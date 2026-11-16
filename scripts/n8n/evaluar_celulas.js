// Lógica del flujo de n8n "Gobierno de TI por célula" (ISO/IEC 38500:2024, tarea Evaluar).
// Sin dependencias: scripts/flujo_gobierno_construir.py copia este archivo dentro de los nodos Code.
// Reglas de cumplimiento y estado iguales a scripts/dashboard_construir.py (rangos del PETI §10).

const MENSAJE_CORREOS = 'Reemplaza los correos de ejemplo en las pestañas Config y Celulas';
const GRAVEDAD = { Bajo: 0, Intermedio: 1, Bueno: 2, 'Sin datos': 3 };

function numero(v) {
  if (v === null || v === undefined) return null;
  const s = String(v).trim().replace(',', '.');
  if (s === '') return null;
  const n = Number(s);
  return Number.isFinite(n) ? n : null;
}

function redondear1(x) {
  return Math.round(x * 10) / 10;
}

function cumplimiento(valor, meta, menorEsMejor) {
  if (valor === null || valor === undefined) return null;
  if (menorEsMejor) return valor <= meta ? 100 : redondear1((100 * meta) / valor);
  return meta ? redondear1(Math.min(100, (100 * valor) / meta)) : 100;
}

function estadoDe(c) {
  if (c === null || c === undefined) return null;
  return c >= 95 ? 'Bueno' : c > 70 ? 'Intermedio' : 'Bajo';
}

function cicloDe(mes) {
  const m0 = 9 + (Number(mes) - 1); // mes 1 = octubre de 2026
  const anio = 2026 + Math.floor(m0 / 12);
  return `${anio}-${String((m0 % 12) + 1).padStart(2, '0')}`;
}

function fmt(valor, unidad) {
  if (valor === null) return 'sin dato';
  return `${valor.toFixed(1).replace('.', ',')} ${unidad}`;
}

function esEjemplo(correo) {
  const c = String(correo || '').trim().toLowerCase();
  return c === '' || c.endsWith('@ejemplo.com');
}

function validarCorreos(config, celulas) {
  const correos = [config.correo_comite, config.correo_copia, ...celulas.map((c) => c.correo_lider)];
  if (correos.some(esEjemplo)) throw new Error(MENSAJE_CORREOS);
}

function evaluarMes(celula, mes, umbrales, mediciones) {
  const filas = mediciones.filter((m) => Number(m.mes) === Number(mes) && m.celula === celula);
  if (filas.length === 0) return { estado: 'Sin datos', indicadores: [] };
  const indicadores = umbrales.map((u) => {
    const fila = filas.find((m) => m.kpi === u.kpi);
    const valor = fila ? numero(fila.valor) : null;
    const meta = numero(u.meta);
    const c = cumplimiento(valor, meta, String(u.menor_es_mejor).trim() === 'Si');
    return { kpi: u.kpi, nombre: u.nombre, valor, meta, unidad: u.unidad, cumplimiento: c, estado: estadoDe(c), proyecto: u.proyecto };
  });
  const conDato = indicadores.filter((i) => i.estado !== null);
  if (conDato.length === 0) return { estado: 'Sin datos', indicadores };
  const peor = conDato.reduce((a, b) => (GRAVEDAD[b.estado] < GRAVEDAD[a.estado] ? b : a));
  return { estado: peor.estado, indicadores };
}

function filasIndicadores(indicadores, soloEstado) {
  return indicadores
    .filter((i) => !soloEstado || soloEstado.includes(i.estado))
    .map((i) => `<tr><td>${i.kpi}</td><td>${i.nombre}</td><td>${fmt(i.valor, i.unidad)}</td><td>${fmt(i.meta, i.unidad)}</td><td>${i.estado || 'sin dato'}</td><td>${i.proyecto}</td></tr>`)
    .join('');
}

const ENCABEZADO = '<tr><th>Indicador</th><th>Nombre</th><th>Valor</th><th>Meta</th><th>Estado</th><th>Proyecto que corrige</th></tr>';

function evaluarCelulas({ config, celulas, umbrales, mediciones, ahora }) {
  const mes = Number(config.mes_corte);
  const ciclo = cicloDe(mes);
  const fecha = ahora || new Date().toISOString();
  return celulas.map((c) => {
    const actual = evaluarMes(c.celula, mes, umbrales, mediciones);
    const anterior = mes > 1 ? evaluarMes(c.celula, mes - 1, umbrales, mediciones).estado : null;
    const item = {
      clave: `${ciclo}|${c.celula}`,
      ciclo,
      celula: c.celula,
      nombre: c.nombre,
      correo_lider: c.correo_lider,
      estado: actual.estado,
      estado_anterior: anterior,
      indicadores: actual.indicadores,
      fecha_ejecucion: fecha,
    };
    for (const u of umbrales) {
      const i = actual.indicadores.find((x) => x.kpi === u.kpi);
      item[u.kpi] = i ? i.valor : null;
    }
    if (actual.estado === 'Intermedio') {
      item.aviso_asunto = `Gobierno de TI ${ciclo}: ${c.celula} con indicadores bajo la meta`;
      item.aviso_html = `<p>La revisión mensual del ciclo ${ciclo} encontró indicadores de ${c.nombre} (${c.celula}) por debajo de la meta del PETI.</p>`
        + `<table border="1" cellpadding="4">${ENCABEZADO}${filasIndicadores(actual.indicadores, ['Intermedio', 'Bajo'])}</table>`
        + '<p>Se pide al Technical Lead y al Line Manager registrar un plan de acción antes del próximo Comité Táctico de TI.</p>';
    }
    return item;
  });
}

function agruparRojos(evaluadas) {
  const rojos = evaluadas.filter((e) => e.estado === 'Bajo');
  if (rojos.length === 0) return [];
  const ciclo = rojos[0].ciclo;
  const n = rojos.length;
  const filas = rojos
    .map((r) => `<tr><td colspan="6"><b>${r.nombre} (${r.celula})</b></td></tr>${filasIndicadores(r.indicadores, ['Bajo'])}`)
    .join('');
  return [{
    ciclo,
    celulas: rojos.map((r) => ({ celula: r.celula, nombre: r.nombre, indicadores: r.indicadores.filter((i) => i.estado === 'Bajo') })),
    asunto: `Aprobación requerida: ${n} ${n === 1 ? 'célula' : 'células'} en rojo, ciclo ${ciclo}`,
    cuerpoHtml: `<p>En el ciclo ${ciclo}, ${n === 1 ? 'una célula tiene' : `${n} células tienen`} indicadores en estado Bajo:</p>`
      + `<table border="1" cellpadding="4">${ENCABEZADO}${filas}</table>`
      + '<p><b>Aprobar</b>: el Comité Táctico de TI ejecuta el plan correctivo del proyecto indicado. '
      + '<b>Escalar</b>: el caso pasa al Comité Directivo del PETI.</p>',
    // El nodo Gmail "Send and Wait" escapa el HTML y respeta los saltos de línea: este es el cuerpo que usa.
    cuerpoTexto: [
      `En el ciclo ${ciclo}, ${n === 1 ? 'una célula tiene' : `${n} células tienen`} indicadores en estado Bajo:`,
      '',
      ...rojos.map((r) => `${r.nombre} (${r.celula}): ${r.indicadores.filter((i) => i.estado === 'Bajo')
        .map((i) => `${i.kpi}: ${fmt(i.valor, i.unidad)} (meta ${fmt(i.meta, i.unidad)}; corrige ${i.proyecto})`).join('; ')}`),
      '',
      'Aprobar plan correctivo: el Comité Táctico de TI ejecuta el plan del proyecto indicado.',
      'Escalar al Comité Directivo: el caso pasa al Comité Directivo del PETI.',
    ].join('\n'),
  }];
}

function armarInforme(evaluadas) {
  const ciclo = evaluadas.length ? evaluadas[0].ciclo : '';
  const minimo = (e) => Math.min(...e.indicadores.filter((i) => i.cumplimiento !== null).map((i) => i.cumplimiento), 101);
  const orden = [...evaluadas].sort((a, b) => GRAVEDAD[a.estado] - GRAVEDAD[b.estado] || minimo(a) - minimo(b));
  const conteo = Object.keys(GRAVEDAD).map((k) => `${k}: ${evaluadas.filter((e) => e.estado === k).length}`).join(' · ');
  const filas = orden
    .map((e) => `<tr><td>${e.celula}</td><td>${e.nombre}</td><td>${e.estado}</td><td>${e.estado_anterior || '—'}</td>`
      + `<td>${e.indicadores.map((i) => `${i.kpi} ${fmt(i.valor, i.unidad)}`).join('<br>')}</td></tr>`)
    .join('');
  return {
    asunto: `Informe mensual de gobierno de TI por célula, ciclo ${ciclo}`,
    cuerpoHtml: `<p>Resultado de la revisión mensual del ciclo ${ciclo} (ISO/IEC 38500:2024: evaluar, dirigir y monitorear).</p>`
      + `<p>${conteo}</p>`
      + '<table border="1" cellpadding="4"><tr><th>Célula</th><th>Nombre</th><th>Estado</th><th>Mes anterior</th><th>Indicadores</th></tr>'
      + `${filas}</table>`
      + '<p>Datos sintéticos del PETI Colombia (trabajo académico). Historial y decisiones en la hoja de gobierno.</p>',
  };
}

function prepararDecisiones(grupo, aprobado, ahora) {
  const decision = aprobado === true ? 'Aprobado plan correctivo'
    : aprobado === false ? 'Escalado al Comité Directivo' : 'Sin respuesta en el plazo';
  return grupo.celulas.map((c) => ({
    fecha: ahora || new Date().toISOString(),
    ciclo: grupo.ciclo,
    celula: c.celula,
    foco: 'Desempeño',
    justificacion: c.indicadores.map((i) => `${i.kpi}: ${fmt(i.valor, i.unidad)} frente a meta ${fmt(i.meta, i.unidad)} (${i.proyecto})`).join('; '),
    decision,
    responsable: 'Comité Táctico de TI',
  }));
}

const COLUMNAS_HISTORIAL = ['clave', 'ciclo', 'celula', 'estado', 'KPI-05', 'ANS', 'KPI-09', 'KPI-10', 'fecha_ejecucion'];

function filaHistorial(item) {
  return Object.fromEntries(COLUMNAS_HISTORIAL.map((k) => [k, item[k] === null || item[k] === undefined ? '' : item[k]]));
}

module.exports = { cumplimiento, estadoDe, validarCorreos, evaluarCelulas, agruparRojos, armarInforme, prepararDecisiones, cicloDe, filaHistorial };
