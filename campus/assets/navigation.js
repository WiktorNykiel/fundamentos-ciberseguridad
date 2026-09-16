/** Navigation derived from the canonical course; no duplicated curriculum. */
import {escapeHTML as e, moduleDone} from './state.js';
export const normalise = value => String(value).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
const href = id => '#/modulo/' + id;
export function introHTML(course) {
  const source = course.resources.find(r => r.title.startsWith('Cómo estudiar'));
  return `<p class="eyebrow">Tu punto de partida</p><h1>Empieza por aquí.</h1>
  <p class="lead">Un mismo recorrido para leer, presentar, practicar y demostrar lo aprendido. No necesitas instalar el campus en cada máquina del laboratorio.</p>
  <div class="blocks">
    <article class="block-card"><span class="pill">1 · Orientarse</span><h2>Elige tu entrada</h2><p>Sin experiencia previa: empieza en M01. Con experiencia: consulta los prerrequisitos y localiza la competencia que quieres reforzar.</p><a href="#/temario">Ver el índice completo →</a></article>
    <article class="block-card"><span class="pill">2 · Preparar</span><h2>Separa web y laboratorio</h2><p>La web guarda tus marcas; Linux, Windows y macOS se practican en máquinas propias y autorizadas. No pegues credenciales ni registros reales en las notas.</p><a href="${href('M01')}">Preparar el entorno →</a></article>
    <article class="block-card"><span class="pill">3 · Aprender</span><h2>Comprende y comprueba</h2><p>Lee la teoría, resuelve la autoevaluación y completa las tres prácticas. En cada una: preparación, ejecución manual, contraste, evidencia y recuperación.</p><a href="#/laboratorios">Abrir las prácticas →</a></article>
    <article class="block-card"><span class="pill">4 · Conservar</span><h2>Continúa otro día</h2><p>Usa favoritos y notas. Exporta tu progreso antes de cambiar de navegador o dominio. Las marcas no equivalen a horas cursadas ni a una certificación.</p><a href="#/progreso">Mi recorrido y copia de progreso →</a></article>
  </div><div class="callout"><strong>Tres formas de seguir la misma lección.</strong> Teoría para estudiar; presentación con flechas y Escape para exponer; asistente por fases para practicar. La presentación no sustituye las evidencias.</div>
  <div class="button-row"><a class="button" href="${href('M01')}">Comenzar M01 →</a>${source?`<a class="button secondary" href="#/recurso/${source.id}">Guía de estudio completa</a>`:''}<a class="button secondary" href="lectura.html">Leer sin JavaScript</a></div>`;
}
export function outlineHTML(course,state) {
  return `<p class="eyebrow">Mapa curricular · fuente única</p><h1>Índice completo del curso.</h1><p class="lead">32 módulos, 96 diseños de práctica y 480 horas planificadas. Acceso directo a teoría, prácticas y autoevaluación; los prerrequisitos orientan, no bloquean.</p>
  <nav class="button-row" aria-label="Saltar a un bloque">${course.blocks.map(b=>`<a class="button secondary" href="#/temario" data-scroll="outline-${b.id}">${e(b.title)}</a>`).join('')}</nav>
  ${course.blocks.map(b=>`<section id="outline-${b.id}"><h2>${e(b.title)} · ${b.hours} h</h2><div class="table-scroll" tabindex="0" role="region" aria-label="Módulos de ${e(b.title)}"><table class="outline-table"><thead><tr><th scope="col">Módulo</th><th scope="col">Teoría / práctica</th><th scope="col">Antes</th><th scope="col">Accesos</th><th scope="col">Avance</th></tr></thead><tbody>${course.modules.filter(m=>m.block===b.id).map(m=>`<tr data-module="${m.id}"><th scope="row"><a href="${href(m.id)}">${m.id} · ${e(m.title)}</a></th><td>${m.theoryHours} h / ${m.practiceHours} h</td><td>${m.prerequisites.length?m.prerequisites.map(id=>`<a href="${href(id)}">${id}</a>`).join(' '):'Sin requisitos'}</td><td><a href="${href(m.id)}">Teoría</a> · <a href="${href(m.id)}/practicas">Prácticas</a> · <a href="${href(m.id)}/revision">Autoevaluación</a></td><td>${moduleDone(m,state)?'Completado por ti':'En curso o pendiente'}</td></tr>`).join('')}</tbody></table></div></section>`).join('')}
  <p class="bottom-note">Las horas son planificación docente, no tiempo medido. Las fichas diseñadas y los ejercicios ejecutados se distinguen en sus evidencias de validación.</p>`;
}
export function searchHTML(course,query) {
  const terms=normalise(query.trim()).split(/\s+/).filter(Boolean).slice(0,12);
  const records=[...course.modules.map(m=>({id:m.id,title:m.title,text:m.search+' '+m.labs.map(l=>l.title+' '+l.tasks).join(' '),url:href(m.id),kind:'Módulo'})),...course.resources.map(r=>({id:r.id,title:r.title,text:r.html.replace(/<[^>]+>/g,' '),url:'#/recurso/'+r.id,kind:'Biblioteca'}))];
  const matches=terms.length?records.filter(r=>terms.every(t=>normalise(r.id+' '+r.title+' '+r.text).includes(t))):[];
  return `<p class="eyebrow">Conceptos, comandos y documentos</p><h1>Resultados de búsqueda.</h1><p class="lead">${terms.length?`${matches.length} resultados para «${e(query)}».`:'Escribe un concepto, un comando o varias palabras.'}</p><div class="search-results">${matches.map(r=>`<a class="search-result" href="${r.url}"><span class="eyebrow">${r.kind} · ${r.id}</span><h2>${e(r.title)}</h2><p>${e(r.text.replace(/\s+/g,' ').trim().slice(0,230))}…</p></a>`).join('')}${terms.length&&!matches.length?'<div class="empty-state"><h2>No hay coincidencias</h2><p>Prueba con «permisos», «PowerShell», «logs» o el código de un módulo.</p><a href="#/temario">Consultar el índice completo</a></div>':''}</div>`;
}
