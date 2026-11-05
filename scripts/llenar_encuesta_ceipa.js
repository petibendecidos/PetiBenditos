// Marca las 33 respuestas del diagnóstico de madurez digital de CEIPA y avanza por las 11 páginas.
//
// Uso: diligenciar a mano los pasos "empresa" y "persona" (datos personales y política de datos),
// llegar a https://api.mdigital.ceipa.edu.co/encuesta, abrir la consola del navegador (F12, pestaña
// "Consola"), pegar este archivo completo y pulsar Enter. Los puntajes y su sustento están en
// docs/entregas-2026-11-04/diagnostico-ceipa/respuestas-diagnostico-ceipa.md.
//
// El formulario de la encuesta tiene id "form" y un grupo de botones de radio por pregunta
// (name = número de pregunta, value = 0 a 10). El script marca los de la página visible, envía el
// formulario y repite con la siguiente. Se detiene si encuentra una pregunta que no conoce.
(() => {
  const respuestas = {
    1: 5, 2: 5, 3: 2, 4: 6, 5: 5, 6: 3, 7: 7, 8: 7, 9: 4,
    10: 2, 11: 5, 12: 2, 13: 7, 14: 4, 15: 4, 16: 5, 17: 3, 18: 3, 19: 7, 20: 5, 21: 2,
    22: 3, 23: 5, 24: 3, 25: 3, 26: 2, 27: 1,
    28: 9, 29: 6, 30: 6, 31: 8, 32: 7, 33: 6,
  };
  const hechas = new Set();

  const paso = (intentos = 0) => {
    if (location.pathname.includes('/encuesta/enviar')) {
      console.log('Encuesta enviada. Espere el radar y guarde la página en PDF.');
      return;
    }
    const form = document.getElementById('form');
    const nombres = form
      ? [...new Set([...form.querySelectorAll('input[type=radio]')].map((i) => i.name))]
      : [];
    // Espera a que se dibuje una página con preguntas que aún no se han marcado.
    if (!nombres.length || nombres.every((n) => hechas.has(n))) {
      if (intentos > 40) return console.warn('No apareció la siguiente página; revise la pantalla.');
      return setTimeout(() => paso(intentos + 1), 250);
    }
    const desconocidas = nombres.filter((n) => !(n in respuestas));
    if (desconocidas.length) {
      return console.error('Preguntas sin respuesta preparada:', desconocidas, '— se detiene.');
    }
    for (const n of nombres) {
      const radio = form.querySelector(`input[name="${n}"][value="${respuestas[n]}"]`);
      if (!radio) return console.error(`No se encontró la opción ${respuestas[n]} de la pregunta ${n}.`);
      radio.click();
      hechas.add(n);
    }
    console.log(`Preguntas ${nombres.join(', ')} marcadas (${hechas.size} de 33).`);
    form.requestSubmit();
    setTimeout(() => paso(), 600);
  };

  paso();
})();
