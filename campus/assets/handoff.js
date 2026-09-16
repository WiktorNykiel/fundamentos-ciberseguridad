/** Portable, non-authenticating progress snapshots. No notes, credentials or network. */
import {validateState, validResumeRoute} from './state.js';
export const HANDOFF_TTL = 7 * 24 * 60 * 60;
export const MAX_CAPSULE = 1400;
const own = (v, keys) => v && typeof v === 'object' && !Array.isArray(v) && Object.keys(v).length===keys.length && Object.keys(v).every(k=>keys.includes(k));
const encode = bytes => btoa(String.fromCharCode(...bytes)).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');
function decode(value, length) {
  if(typeof value!=='string'||value.length>MAX_CAPSULE||!/^[A-Za-z0-9_-]+$/.test(value))throw new Error('Invalid transfer encoding');
  let bytes;try{bytes=Uint8Array.from(atob(value.replace(/-/g,'+').replace(/_/g,'/')),c=>c.charCodeAt(0));}catch{throw new Error('Invalid transfer encoding');}
  if(encode(bytes)!==value || (length!==undefined&&bytes.length!==length))throw new Error('Invalid transfer size');
  return bytes;
}
function catalogue(course) {
  if(course.id!=='fundamentos-ciberseguridad'||course.modules.length!==32)throw new Error('Incompatible course');
  course.modules.forEach((m,i)=>{
    const n=String(i+1).padStart(2,'0');
    if(m.id!=='M'+n||m.labs.length!==3||m.labs.some((l,j)=>l.id!==`L${n}${'ABC'[j]}`))throw new Error('Incompatible course identifiers');
  });
}
function pack(flags) {
  const data=new Uint8Array(Math.ceil(flags.length/8));
  flags.forEach((v,i)=>{if(v)data[i>>3]|=1<<(i%8);});
  return encode(data);
}
function unpack(value,count) {
  const data=decode(value,Math.ceil(count/8));
  return Array.from({length:count},(_,i)=>Boolean(data[i>>3]&(1<<(i%8))));
}
export function createCapsule(course, state, lang='es', now=Math.floor(Date.now()/1000)) {
  catalogue(course);if(!Number.isSafeInteger(now)||now<0)throw new Error('Invalid transfer date');if(!['es','en'].includes(lang))throw new Error('Invalid transfer language');
  const clean=validateState(state,course);
  const m=course.modules.flatMap(m=>{const s=clean.modules[m.id];return [s.read,s.quiz,s.bookmarked];});
  const l=course.modules.flatMap(m=>m.labs.flatMap(l=>{const s=clean.labs[l.id];return [...s.steps,s.done];}));
  const payload={v:1,c:course.id,t:now,x:now+HANDOFF_TTL,lang,r:clean.lastRoute,m:pack(m),l:pack(l)};
  return encode(new TextEncoder().encode(JSON.stringify(payload)));
}
export function readCapsule(text, course, now=Math.floor(Date.now()/1000)) {
  catalogue(course);
  const payload=JSON.parse(new TextDecoder('utf-8',{fatal:true}).decode(decode(text)));
  if(!own(payload,['v','c','t','x','lang','r','m','l'])||payload.v!==1||payload.c!==course.id||!['es','en'].includes(payload.lang))throw new Error('Incompatible transfer');
  if(!Number.isSafeInteger(payload.t)||!Number.isSafeInteger(payload.x)||payload.t<0||payload.t>now+300||payload.x<=now||payload.x-payload.t!==HANDOFF_TTL)throw new Error('Expired or invalid transfer date');
  if(!validResumeRoute(payload.r,course))throw new Error('Invalid continuation route');
  const modules=unpack(payload.m,96),labs=unpack(payload.l,576);
  for(let i=0;i<96;i++)if(labs[i*6+5]&&!labs.slice(i*6,i*6+5).every(Boolean))throw new Error('Inconsistent transferred lab');
  return {route:payload.r,language:payload.lang,issued:payload.t,expires:payload.x,modules,labs};
}
export function mergeCapsule(course,state,capsule) {
  catalogue(course);
  if(!own(capsule,['route','language','issued','expires','modules','labs'])||!validResumeRoute(capsule.route,course)||!['es','en'].includes(capsule.language)||!Array.isArray(capsule.modules)||capsule.modules.length!==96||!Array.isArray(capsule.labs)||capsule.labs.length!==576||[...capsule.modules,...capsule.labs].some(x=>typeof x!=='boolean'))throw new Error('Invalid transfer data');
  if(!Number.isSafeInteger(capsule.issued)||!Number.isSafeInteger(capsule.expires)||capsule.expires<=Math.floor(Date.now()/1000)||capsule.expires-capsule.issued!==HANDOFF_TTL)throw new Error('Expired transfer');
  const next=validateState(state,course);
  course.modules.forEach((m,i)=>{
    const item=next.modules[m.id];['read','quiz','bookmarked'].forEach((k,j)=>item[k] ||= capsule.modules[i*3+j]);
    m.labs.forEach((l,j)=>{
      const offset=(i*3+j)*6, entry=next.labs[l.id];
      entry.steps=entry.steps.map((v,k)=>v||capsule.labs[offset+k]);
      if(capsule.labs[offset+5]&&!capsule.labs.slice(offset,offset+5).every(Boolean))throw new Error('Inconsistent transferred lab');
      entry.done=entry.done||capsule.labs[offset+5];
    });
  });
  next.lastRoute=capsule.route;
  next.updatedAt=new Date().toISOString();
  return validateState(next,course);
}
export function continuationURL(base,course,state,lang,now) {
  const u=new URL(base);
  if(u.protocol!=='https:' && !(u.protocol==='http:' && ['127.0.0.1','localhost','[::1]'].includes(u.hostname)))throw new Error('Use HTTPS to share the campus');
  if(u.username||u.password)throw new Error('Credential-bearing URLs are not allowed');
  u.search='';u.searchParams.set('lang',lang);u.hash='/transfer/'+createCapsule(course,state,lang,now);
  if(u.href.length>2048)throw new Error('Transfer link is too long');
  return u.href;
}
