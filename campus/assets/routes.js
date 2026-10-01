/** Optional local self-assessment. No identity, notes, imports, network or legal decisions. */
const KEY='smartkea.learning-paths.v1';
const routes=[...document.querySelectorAll('[data-route]')];
const phases=[...document.querySelectorAll('[data-phase]')];
const allowed=new Set(phases.map(p=>p.dataset.phase));
const remember=document.querySelector('#remember-paths');
const status=document.querySelector('#path-status');
const select=document.querySelector('#route-filter');
let slide=0;
function progress(){for(const route of routes){const checks=[...route.querySelectorAll('[data-phase]')];route.querySelector('[data-progress]').textContent=`${checks.filter(p=>p.checked).length} de ${checks.length} etapas revisadas`;}}
function save(){
 progress();if(!remember.checked)return;
 try{localStorage.setItem(KEY,JSON.stringify({schema:1,completed:phases.filter(p=>p.checked).map(p=>p.dataset.phase)}));status.textContent='Marcas guardadas solo en este navegador. Sin sincronización ni datos personales.';}
 catch{remember.checked=false;status.textContent='El navegador no permite guardar. Las marcas siguen disponibles solo durante esta visita.';}
}
function filter(id){
 if(id!=='all'&&!routes.some(r=>r.dataset.route===id))id='all';
 select.value=id;for(const r of routes)r.hidden=id!=='all'&&r.dataset.route!==id;
 history.replaceState(null,'',location.pathname+location.search+(id==='all'?'':'#ruta-'+id));
}
function showSlide(){routes.forEach((r,i)=>{r.hidden=false;r.classList.toggle('presenting',i===slide);});document.querySelector('#slide-count').textContent=`Ruta ${slide+1} de ${routes.length}`;window.scrollTo(0,0);}
function exit(){document.body.classList.remove('presentation');routes.forEach(r=>r.classList.remove('presenting'));filter(select.value);document.querySelector('#start-presentation').focus();}
try{const raw=localStorage.getItem(KEY);if(raw&&raw.length<20000){const state=JSON.parse(raw);if(state.schema===1&&Array.isArray(state.completed)&&state.completed.length<=allowed.size&&state.completed.every(p=>typeof p==='string'&&allowed.has(p))){const done=new Set(state.completed);phases.forEach(p=>p.checked=done.has(p.dataset.phase));remember.checked=true;status.textContent='Marcas recuperadas de este navegador; no son una certificación.';}}}catch{status.textContent='No se pudo leer el almacenamiento local. Puedes seguir sin guardar.';}
phases.forEach(p=>p.addEventListener('change',save));
remember.addEventListener('change',()=>{if(remember.checked)save();else{try{localStorage.removeItem(KEY);status.textContent='Guardado desactivado y copia local eliminada. Marcas solo para esta visita.';}catch{status.textContent='No fue posible eliminar la copia local. Revisa el almacenamiento del navegador.';}}});
document.querySelector('#clear-paths').addEventListener('click',()=>{if(!window.confirm('¿Borrar únicamente las marcas de estas rutas? Las notas y el progreso del campus no se modificarán.'))return;phases.forEach(p=>p.checked=false);remember.checked=false;try{localStorage.removeItem(KEY);status.textContent='Marcas de rutas borradas. El campus no se ha modificado.';}catch{status.textContent='Marcas de la visita borradas; no se pudo eliminar la copia del navegador.';}progress();});
select.addEventListener('change',()=>filter(select.value));
document.querySelectorAll('[data-route-select]').forEach(b=>b.addEventListener('click',()=>{filter(b.dataset.routeSelect);document.querySelector('#ruta-'+b.dataset.routeSelect).scrollIntoView({block:'start'});}));
document.querySelector('#print-paths').addEventListener('click',()=>window.print());
document.querySelector('#start-presentation').addEventListener('click',()=>{slide=Math.max(0,routes.findIndex(r=>r.dataset.route===select.value));document.body.classList.add('presentation');showSlide();document.querySelector('#next-route').focus();});
document.querySelector('#next-route').addEventListener('click',()=>{slide=(slide+1)%routes.length;showSlide();});
document.querySelector('#previous-route').addEventListener('click',()=>{slide=(slide+routes.length-1)%routes.length;showSlide();});
document.querySelector('#exit-presentation').addEventListener('click',exit);
document.addEventListener('keydown',e=>{if(!document.body.classList.contains('presentation')||/INPUT|SELECT|TEXTAREA/.test(e.target.tagName))return;if(e.key==='Escape'){e.preventDefault();exit();}else if(e.key==='ArrowRight'||e.key==='ArrowLeft'){e.preventDefault();slide=(slide+(e.key==='ArrowRight'?1:routes.length-1))%routes.length;showSlide();}});
const initial=location.hash.startsWith('#ruta-')?location.hash.slice(6):'all';filter(initial);progress();
