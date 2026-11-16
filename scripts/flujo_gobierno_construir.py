"""Construye el JSON de n8n del flujo "Gobierno de TI por célula" (ISO/IEC 38500:2024).

Uso:
    python scripts/flujo_gobierno_construir.py <salida.json>
        [--spreadsheet-id X --credencial-sheets Y --credencial-gmail Z]

Sin argumentos deja los marcadores __SPREADSHEET_ID__, __CREDENCIAL_SHEETS__ y __CREDENCIAL_GMAIL__: esa es la
versión que va al repositorio. Con argumentos produce la copia para importar (fuera del repositorio, en
D:\\dev\\n8n\\peti\\). La lógica de los nodos Code sale de scripts/n8n/evaluar_celulas.js (probada con node --test)
y se copia entera en cada nodo, sin la línea module.exports. Los correos no van en el flujo: se leen de la hoja.

Tipos y versiones de nodos de n8n 2.47.7; ver la skill flujos-n8n ("Nodos confirmados").
"""
import argparse
import json
import re
import uuid
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
MODULO = RAIZ / "n8n" / "evaluar_celulas.js"
NOMBRE = "Gobierno de TI por célula (ISO/IEC 38500:2024)"
CRED_SHEETS = "Google Sheets PETI"
CRED_GMAIL = "Gmail PETI"


def modulo_js() -> str:
    texto = MODULO.read_text(encoding="utf8")
    return re.sub(r"^module\.exports\s*=.*$", "", texto, flags=re.M).strip()


def nodo(nombre, tipo, version, x, y, parametros, **extra):
    n = {"id": str(uuid.uuid5(uuid.NAMESPACE_URL, f"peti-gobierno/{nombre}")), "name": nombre, "type": tipo,
         "typeVersion": version, "position": [x, y], "parameters": parametros}
    n.update(extra)
    return n


def hoja(spreadsheet_id, cred_sheets, nombre, pestana, x, y, una_vez=True, **parametros):
    base = {"authentication": "oAuth2",
            "documentId": {"__rl": True, "value": spreadsheet_id, "mode": "id"},
            "sheetName": {"__rl": True, "value": pestana, "mode": "name"}}
    base.update(parametros)
    extra = {"credentials": {"googleSheetsOAuth2Api": {"id": cred_sheets, "name": CRED_SHEETS}}}
    if una_vez:
        extra["executeOnce"] = True
    return nodo(nombre, "n8n-nodes-base.googleSheets", 4.7, x, y, base, **extra)


def codigo(nombre, x, y, cuerpo, con_modulo=True):
    js = (modulo_js() + "\n\n" if con_modulo else "") + cuerpo.strip()
    return nodo(nombre, "n8n-nodes-base.code", 2, x, y, {"mode": "runOnceForAllItems", "language": "javaScript", "jsCode": js})


def gmail(cred_gmail, nombre, x, y, parametros):
    return nodo(nombre, "n8n-nodes-base.gmail", 2.1, x, y, parametros,
                credentials={"gmailOAuth2": {"id": cred_gmail, "name": CRED_GMAIL}}, webhookId=str(uuid.uuid5(uuid.NAMESPACE_URL, nombre)))


def condicion_estado(valor):
    return {
        "conditions": {
            "options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict", "version": 2},
            "conditions": [{"id": str(uuid.uuid5(uuid.NAMESPACE_URL, valor)), "leftValue": "={{ $json.estado }}",
                            "rightValue": valor, "operator": {"type": "string", "operation": "equals"}}],
            "combinator": "and",
        },
        "renameOutput": True,
        "outputKey": valor,
    }


def construir(salida, spreadsheet_id="__SPREADSHEET_ID__", credencial_sheets="__CREDENCIAL_SHEETS__",
              credencial_gmail="__CREDENCIAL_GMAIL__"):
    s, cs, cg = spreadsheet_id, credencial_sheets, credencial_gmail
    comite = "={{ $('Leer Config').first().json.correo_comite }}"
    nodos = [
        nodo("Disparo mensual", "n8n-nodes-base.scheduleTrigger", 1.2, 0, 0,
             {"rule": {"interval": [{"field": "months", "monthsInterval": 1, "triggerAtDayOfMonth": 1, "triggerAtHour": 7}]}}),
        nodo("Disparo manual", "n8n-nodes-base.manualTrigger", 1, 0, 200, {}),
        hoja(s, cs, "Leer Config", "Config", 240, 100, una_vez=False, operation="read", options={}),
        hoja(s, cs, "Leer Células", "Celulas", 460, 100, operation="read", options={}),
        hoja(s, cs, "Leer Umbrales", "Umbrales", 680, 100, operation="read", options={}),
        hoja(s, cs, "Leer Mediciones", "Mediciones", 900, 100, operation="read", options={}),
        codigo("Evaluar células", 1120, 100, """
const config = $('Leer Config').first().json;
const celulas = $('Leer Células').all().map((i) => i.json);
const umbrales = $('Leer Umbrales').all().map((i) => i.json);
const mediciones = $('Leer Mediciones').all().map((i) => i.json);
validarCorreos(config, celulas);
return evaluarCelulas({ config, celulas, umbrales, mediciones }).map((json) => ({ json }));
"""),
        codigo("Preparar historial", 1360, -120, "return $input.all().map((i) => ({ json: filaHistorial(i.json) }));"),
        hoja(s, cs, "Registrar historial", "Historial", 1580, -120, una_vez=False, operation="appendOrUpdate",
             columns={"mappingMode": "autoMapInputData", "value": {}, "matchingColumns": ["clave"], "schema": []},
             options={"cellFormat": "RAW"}),
        nodo("Según estado", "n8n-nodes-base.switch", 3.2, 1360, 100,
             {"rules": {"values": [condicion_estado("Intermedio"), condicion_estado("Bajo")]}, "options": {}}),
        gmail(cg, "Avisar a líderes", 1580, 20, {
            "sendTo": "={{ $json.correo_lider }}", "subject": "={{ $json.aviso_asunto }}",
            "emailType": "html", "message": "={{ $json.aviso_html }}", "options": {"appendAttribution": False}}),
        codigo("Agrupar rojos", 1580, 200,
               "return agruparRojos($input.all().map((i) => i.json)).map((json) => ({ json }));"),
        gmail(cg, "Aprobación del Comité", 1800, 200, {
            "operation": "sendAndWait", "sendTo": comite, "subject": "={{ $json.asunto }}",
            "message": "={{ $json.cuerpoTexto }}",  # este nodo escapa el HTML y respeta los saltos de línea
            "approvalOptions": {"values": {"approvalType": "double", "approveLabel": "Aprobar plan correctivo",
                                           "disapproveLabel": "Escalar al Comité Directivo"}},
            "options": {"limitWaitTime": {"values": {"limitType": "afterTimeInterval", "resumeAmount": 3, "resumeUnit": "days"}},
                        "appendAttribution": False}}),
        codigo("Preparar decisión", 2020, 200, """
const grupo = $('Agrupar rojos').first().json;
const r = $input.first().json;
const aprobado = r.data && typeof r.data.approved === 'boolean' ? r.data.approved : null;
return prepararDecisiones(grupo, aprobado).map((json) => ({ json }));
"""),
        hoja(s, cs, "Registrar decisión", "Decisiones", 2240, 200, una_vez=False, operation="append",
             columns={"mappingMode": "autoMapInputData", "value": {}, "schema": []}, options={"cellFormat": "RAW"}),
        codigo("Armar informe", 1360, 340, "return [{ json: armarInforme($input.all().map((i) => i.json)) }];"),
        gmail(cg, "Enviar informe", 1580, 340, {
            "sendTo": "={{ $('Leer Config').first().json.correo_comite }},{{ $('Leer Config').first().json.correo_copia }}",
            "subject": "={{ $json.asunto }}", "emailType": "html", "message": "={{ $json.cuerpoHtml }}",
            "options": {"appendAttribution": False}}),
    ]

    def a(*destinos):
        return {"main": [[{"node": d, "type": "main", "index": 0} for d in destinos]]}

    conexiones = {
        "Disparo mensual": a("Leer Config"),
        "Disparo manual": a("Leer Config"),
        "Leer Config": a("Leer Células"),
        "Leer Células": a("Leer Umbrales"),
        "Leer Umbrales": a("Leer Mediciones"),
        "Leer Mediciones": a("Evaluar células"),
        "Evaluar células": a("Preparar historial", "Según estado", "Armar informe"),
        "Preparar historial": a("Registrar historial"),
        "Según estado": {"main": [[{"node": "Avisar a líderes", "type": "main", "index": 0}],
                                  [{"node": "Agrupar rojos", "type": "main", "index": 0}]]},
        "Agrupar rojos": a("Aprobación del Comité"),
        "Aprobación del Comité": a("Preparar decisión"),
        "Preparar decisión": a("Registrar decisión"),
        "Armar informe": a("Enviar informe"),
    }
    flujo = {"name": NOMBRE, "nodes": nodos, "connections": conexiones, "active": False, "pinData": {},
             "settings": {"executionOrder": "v1", "timezone": "America/Bogota"}}
    salida = Path(salida)
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(json.dumps(flujo, ensure_ascii=False, indent=2), encoding="utf8")
    return salida


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("salida")
    ap.add_argument("--spreadsheet-id", default="__SPREADSHEET_ID__")
    ap.add_argument("--credencial-sheets", default="__CREDENCIAL_SHEETS__")
    ap.add_argument("--credencial-gmail", default="__CREDENCIAL_GMAIL__")
    a = ap.parse_args()
    print("ok", construir(a.salida, a.spreadsheet_id, a.credencial_sheets, a.credencial_gmail))


if __name__ == "__main__":
    main()
