/** Estado local versionado. El avance es autodeclarado, no acreditación. */
export const KEY = 'fundamentos-ciberseguridad:progress:v1';
export const MAX_IMPORT = 200000;
const plain = v => v !== null && typeof v === 'object' && !Array.isArray(v) && [Object.prototype, null].includes(Object.getPrototypeOf(v));
const allowed = (o, keys) => plain(o) && Object.keys(o).every(k => keys.includes(k));
export function emptyState(course) {
  return {schemaVersion: 1, courseId: course.id, updatedAt: new Date().toISOString(), lastRoute: '#/modulo/M01',
    modules: Object.fromEntries(course.modules.map(m => [m.id, {read: false, quiz: false, bookmarked: false, notes: ''}])),
    labs: Object.fromEntries(course.modules.flatMap(m => m.labs.map(l => [l.id, {steps: [false,false,false,false,false], done: false}]))),
    preferences: {platform: 'linux', largeText: false}};
}
export function validateState(value, course) {
  if (!allowed(value, ['schemaVersion','courseId','updatedAt','lastRoute','modules','labs','preferences']) || value.schemaVersion !== 1 || value.courseId !== course.id) throw new Error('La copia no corresponde a este curso o versión de progreso.');
  const output = emptyState(course);
  if (!plain(value.modules) || !plain(value.labs)) throw new Error('Estructura de progreso inválida.');
  if (Object.keys(value.modules).some(k => !Object.hasOwn(output.modules,k)) || Object.keys(value.labs).some(k => !Object.hasOwn(output.labs,k))) throw new Error('La copia contiene módulos o prácticas desconocidos.');
  for (const [id, item] of Object.entries(value.modules)) {
    if (!allowed(item,['read','quiz','bookmarked','notes']) || !['read','quiz','bookmarked'].every(k => typeof item[k] === 'boolean') || typeof item.notes !== 'string' || item.notes.length > 3000) throw new Error('Datos del módulo no válidos.');
    output.modules[id] = {read:item.read,quiz:item.quiz,bookmarked:item.bookmarked,notes:item.notes};
  }
  for (const [id,item] of Object.entries(value.labs)) {
    if (!allowed(item,['steps','done']) || !Array.isArray(item.steps) || item.steps.length !== 5 || item.steps.some(v => typeof v !== 'boolean') || typeof item.done !== 'boolean' || (item.done && !item.steps.every(Boolean))) throw new Error('Estado de práctica incoherente.');
    output.labs[id] = {steps:[...item.steps],done:item.done};
  }
  if (value.preferences !== undefined) {
    if (!allowed(value.preferences,['platform','largeText']) || !['linux','windows','macos'].includes(value.preferences.platform) || typeof value.preferences.largeText !== 'boolean') throw new Error('Preferencias inválidas.');
    output.preferences = {...value.preferences};
  }
  if (typeof value.lastRoute === 'string' && /^#\/modulo\/M\d{2}(?:\/practica\/L\d{2}[ABC])?$/.test(value.lastRoute)) {
    const parts=value.lastRoute.split('/'); const module=course.modules.find(m=>m.id===parts[2]);
    if (module && (!parts[4] || module.labs.some(l=>l.id===parts[4]))) output.lastRoute=value.lastRoute;
  }
  if (typeof value.updatedAt === 'string' && /^\d{4}-\d{2}-\d{2}T/.test(value.updatedAt) && Number.isFinite(Date.parse(value.updatedAt))) output.updatedAt=value.updatedAt;
  return output;
}
export function parseImport(text, course) {
  if (typeof text !== 'string' || text.length > MAX_IMPORT) throw new Error('Archivo demasiado grande (máximo 200 KB).');
  return validateState(JSON.parse(text), course);
}
export function progress(course, state) {
  let checked=0, completed=0, read=0, labs=0;
  for (const m of course.modules) {
    const ms=state.modules[m.id]; const n=m.labs.filter(l=>state.labs[l.id].done).length;
    checked+=Number(ms.read)+Number(ms.quiz)+n; read+=Number(ms.read); labs+=n;
    if (ms.read && ms.quiz && n===m.labs.length) completed++;
  }
  const total=course.modules.reduce((sum,m)=>sum+2+m.labs.length,0);
  return {checked,total,completed,read,labs,percent:Math.round(100*checked/total)};
}
export function moduleDone(m,state) {return state.modules[m.id].read && state.modules[m.id].quiz && m.labs.every(l=>state.labs[l.id].done);}
export function escapeHTML(value) {return String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
