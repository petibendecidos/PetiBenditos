// Pruebas de la lógica del flujo de gobierno de TI por célula. Ejecutar: node --test scripts/n8n/
const test = require('node:test');
const assert = require('node:assert/strict');
const {
  cumplimiento, estadoDe, validarCorreos, evaluarCelulas, agruparRojos, armarInforme, prepararDecisiones, filaHistorial,
} = require('./evaluar_celulas.js');

const UMBRALES = [
  { kpi: 'KPI-05', nombre: 'Remediación de vulnerabilidades críticas', meta: 72, menor_es_mejor: 'Si', unidad: 'h', proyecto: 'P2.2, P2.3' },
  { kpi: 'ANS', nombre: 'Tickets dentro del ANS', meta: 90, menor_es_mejor: 'No', unidad: '%', proyecto: 'P2.5' },
];
const CONFIG = { mes_corte: 12, correo_comite: 'comite@equipo.co', correo_copia: 'copia@equipo.co' };
const CELULAS = [
  { celula: 'C01', nombre: 'Célula 01', correo_lider: 'lider@equipo.co' },
  { celula: 'C05', nombre: 'Célula 05', correo_lider: 'lider@equipo.co' },
];
const AHORA = '2027-10-01T12:00:00.000Z';

function med(mes, celula, kpi, valor) {
  return { mes, etiqueta: '', celula, kpi, valor, n: 1 };
}

function evaluar(mediciones, celulas = CELULAS) {
  return evaluarCelulas({ config: CONFIG, celulas, umbrales: UMBRALES, mediciones, ahora: AHORA });
}

test('cumplimiento con menor es mejor y mayor es mejor', () => {
  assert.equal(cumplimiento(181, 72, true), 39.8);
  assert.equal(cumplimiento(60, 72, true), 100);
  assert.equal(cumplimiento(63, 90, false), 70);
  assert.equal(cumplimiento(95, 90, false), 100);
  assert.equal(cumplimiento(null, 72, true), null);
});

test('estado con los rangos del PETI §10', () => {
  assert.equal(estadoDe(95), 'Bueno');
  assert.equal(estadoDe(70.1), 'Intermedio');
  assert.equal(estadoDe(70), 'Bajo');
  assert.equal(estadoDe(null), null);
});

test('KPI-05 sin dato no cuenta como Bueno y el estado sale de los demás', () => {
  const [c01] = evaluar([med(12, 'C01', 'KPI-05', ''), med(12, 'C01', 'ANS', 96)], [CELULAS[0]]);
  assert.equal(c01.estado, 'Bueno');
  const kpi05 = c01.indicadores.find((i) => i.kpi === 'KPI-05');
  assert.equal(kpi05.valor, null);
  assert.equal(kpi05.estado, null);
});

test('célula sin mediciones en el mes de corte queda Sin datos', () => {
  const [c01] = evaluar([med(11, 'C01', 'ANS', 96)], [CELULAS[0]]);
  assert.equal(c01.estado, 'Sin datos');
});

test('el peor indicador define el estado, con clave y ciclo del mes 12', () => {
  const res = evaluar([
    med(12, 'C05', 'KPI-05', 181), med(12, 'C05', 'ANS', 96),
    med(11, 'C05', 'KPI-05', 80), med(11, 'C05', 'ANS', 96),
  ], [CELULAS[1]]);
  assert.equal(res[0].estado, 'Bajo');
  assert.equal(res[0].ciclo, '2027-09');
  assert.equal(res[0].clave, '2027-09|C05');
  assert.equal(res[0].estado_anterior, 'Intermedio');
  assert.equal(res[0]['KPI-05'], 181);
  assert.equal(res[0].fecha_ejecucion, AHORA);
});

test('el ciclo del mes 1 es octubre de 2026', () => {
  const res = evaluarCelulas({ config: { ...CONFIG, mes_corte: 1 }, celulas: [CELULAS[0]], umbrales: UMBRALES,
    mediciones: [med(1, 'C01', 'ANS', 96)], ahora: AHORA });
  assert.equal(res[0].ciclo, '2026-10');
});

test('valores con coma decimal se leen como número', () => {
  const [c01] = evaluar([med(12, 'C01', 'ANS', '80,5')], [CELULAS[0]]);
  assert.equal(c01.ANS, 80.5);
  assert.equal(c01.estado, 'Intermedio');
});

test('una célula en Intermedio lleva el aviso para sus líderes', () => {
  const [c01] = evaluar([med(12, 'C01', 'ANS', 80)], [CELULAS[0]]);
  assert.equal(c01.estado, 'Intermedio');
  assert.match(c01.aviso_asunto, /C01/);
  assert.match(c01.aviso_html, /80,0 %/);
});

test('agruparRojos sin rojos devuelve una lista vacía', () => {
  const res = evaluar([med(12, 'C01', 'ANS', 96), med(12, 'C05', 'ANS', 96)]);
  assert.deepEqual(agruparRojos(res), []);
});

test('agruparRojos junta los rojos en una sola solicitud', () => {
  const res = evaluar([med(12, 'C01', 'KPI-05', 200), med(12, 'C05', 'KPI-05', 181)]);
  const grupos = agruparRojos(res);
  assert.equal(grupos.length, 1);
  assert.equal(grupos[0].celulas.length, 2);
  assert.match(grupos[0].asunto, /2 células/);
  assert.match(grupos[0].cuerpoHtml, /181,0 h/);
});

test('la solicitud de aprobación trae una versión en texto plano, sin etiquetas HTML', () => {
  const res = evaluar([med(12, 'C05', 'KPI-05', 181)]);
  const [grupo] = agruparRojos(res);
  assert.doesNotMatch(grupo.cuerpoTexto, /<[a-z]/i);
  assert.match(grupo.cuerpoTexto, /C05/);
  assert.match(grupo.cuerpoTexto, /KPI-05: 181,0 h \(meta 72,0 h; corrige P2\.2, P2\.3\)/);
  assert.match(grupo.cuerpoTexto, /\n/);
});

test('armarInforme ordena de peor a mejor y cuenta por estado', () => {
  const res = evaluar([med(12, 'C01', 'ANS', 96), med(12, 'C05', 'KPI-05', 181)]);
  const informe = armarInforme(res);
  assert.match(informe.asunto, /2027-09/);
  assert.ok(informe.cuerpoHtml.indexOf('C05') < informe.cuerpoHtml.indexOf('C01'));
  assert.match(informe.cuerpoHtml, /Bajo: 1/);
  assert.match(informe.cuerpoHtml, /Bueno: 1/);
});

test('prepararDecisiones registra la decisión de cada célula en rojo', () => {
  const res = evaluar([med(12, 'C01', 'KPI-05', 200), med(12, 'C05', 'KPI-05', 181)]);
  const [grupo] = agruparRojos(res);
  const aprobadas = prepararDecisiones(grupo, true, AHORA);
  assert.equal(aprobadas.length, 2);
  assert.equal(aprobadas[0].decision, 'Aprobado plan correctivo');
  assert.equal(aprobadas[0].responsable, 'Comité Táctico de TI');
  assert.match(aprobadas[0].justificacion, /KPI-05/);
  assert.equal(prepararDecisiones(grupo, false, AHORA)[0].decision, 'Escalado al Comité Directivo');
  assert.equal(prepararDecisiones(grupo, null, AHORA)[0].decision, 'Sin respuesta en el plazo');
});

test('filaHistorial deja solo las columnas de la pestaña Historial', () => {
  const [c05] = evaluar([med(12, 'C05', 'KPI-05', 181)], [CELULAS[1]]);
  assert.deepEqual(filaHistorial(c05), {
    clave: '2027-09|C05', ciclo: '2027-09', celula: 'C05', estado: 'Bajo',
    'KPI-05': 181, ANS: '', 'KPI-09': '', 'KPI-10': '', fecha_ejecucion: AHORA,
  });
});

test('validarCorreos detiene el flujo con correos de ejemplo', () => {
  const msg = 'Reemplaza los correos de ejemplo en las pestañas Config y Celulas';
  assert.throws(() => validarCorreos({ ...CONFIG, correo_comite: 'comite@ejemplo.com' }, CELULAS), { message: msg });
  assert.throws(() => validarCorreos(CONFIG, [{ celula: 'C01', correo_lider: '' }]), { message: msg });
  assert.doesNotThrow(() => validarCorreos(CONFIG, CELULAS));
});
