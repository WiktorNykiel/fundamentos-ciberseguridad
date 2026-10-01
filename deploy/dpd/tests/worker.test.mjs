import test from 'node:test';
import assert from 'node:assert/strict';
import worker, {PREFIX, CSP} from '../worker.mjs';
const call=(path,env={},init={})=>worker.fetch(new Request('https://smartkea.com'+path,init),env);
const good={ASSETS:{fetch:async()=>new Response('ok',{headers:{'Content-Type':'text/html','Set-Cookie':'unwanted=1','Access-Control-Allow-Origin':'*'}})}};
for (const path of ['/', '/assets/app.js', '/introduccion-dpdx', '/introduccion-dpd-old/', '/introduccion-informatica/']) {
  test('rejects unrelated path '+path, async()=>assert.equal((await call(path,good)).status,404));
}
for (const method of ['POST','PUT','PATCH','DELETE','OPTIONS']) {
  test('read-only '+method, async()=>{
    const res=await call(PREFIX+'/',good,{method}); assert.equal(res.status,405); assert.equal(res.headers.get('allow'),'GET, HEAD');
  });
}
for (const path of ['/a%2Fb','/.hidden','/a//b','/x%20y']) {
  test('rejects ambiguous filename '+path, async()=>assert.equal((await call(PREFIX+path,good)).status,404));
}
test('canonical slash preserves query in redirect',async()=>{
  const res=await call(PREFIX+'?lang=en'); assert.equal(res.status,308);assert.equal(res.headers.get('location'),PREFIX+'/?lang=en');
});
test('mount preserves prefix and strips query, cookies and auth for ASSETS',async()=>{
  let internal;
  const env={ASSETS:{fetch:async req=>{internal=req;return new Response('ok')}}};
  const res=await call(PREFIX+'/?x=1',env,{headers:{Cookie:'private=1',Authorization:'Bearer dummy','If-None-Match':'abc'}});
  assert.equal(res.status,200); assert.equal(new URL(internal.url).pathname,PREFIX+'/index.html');assert.equal(new URL(internal.url).search,'');
  assert.equal(internal.headers.get('cookie'),null);assert.equal(internal.headers.get('authorization'),null);assert.equal(internal.headers.get('if-none-match'),'abc');
});
test('headers applied, no cookies or permissive CORS',async()=>{
  const res=await call(PREFIX+'/',good);assert.equal(res.headers.get('content-security-policy'),CSP);assert.equal(res.headers.get('x-content-type-options'),'nosniff');
  assert.equal(res.headers.get('set-cookie'),null);assert.equal(res.headers.get('access-control-allow-origin'),null);assert.equal(res.headers.get('cache-control'),'no-cache');
});
test('missing asset is a real 404',async()=>{
 const res=await call(PREFIX+'/missing.js',{ASSETS:{fetch:async()=>new Response('missing',{status:404})}});assert.equal(res.status,404);assert.equal(res.headers.get('cache-control'),'no-store');
});
test('HEAD contains no response body',async()=>{const res=await call(PREFIX+'/',good,{method:'HEAD'});assert.equal(res.status,200);assert.equal(await res.text(),'')});
test('conditional 304 is preserved',async()=>{
 const res=await call(PREFIX+'/a.js',{ASSETS:{fetch:async()=>new Response(null,{status:304,headers:{ETag:'abc'}})}});assert.equal(res.status,304);assert.equal(res.headers.get('etag'),'abc');
});
test('missing binding returns 503',async()=>assert.equal((await call(PREFIX+'/')).status,503));
test('asset failure returns 503 without leaking exception',async()=>{
 const res=await call(PREFIX+'/',{ASSETS:{fetch:async()=>{throw new Error('private exception')}}});assert.equal(res.status,503);assert.ok(!(await res.text()).includes('private exception'));
});
test('unexpected asset redirects fail closed',async()=>assert.equal((await call(PREFIX+'/',{ASSETS:{fetch:async()=>new Response(null,{status:302,headers:{location:'https://example.org'}})}})).status,502));
test('health reports asset release but does not claim verified deployment',async()=>{
 const release={application:'introduccion-dpd',treeSha256:'a'.repeat(64),deploymentVerified:false};
 const res=await call(PREFIX+'/healthz',{ASSETS:{fetch:async()=>Response.json(release)}});assert.equal(res.status,200);assert.equal(res.headers.get('cache-control'),'no-store');assert.equal((await res.json()).deploymentVerified,false);
});
test('health missing metadata is 503',async()=>assert.equal((await call(PREFIX+'/healthz',{ASSETS:{fetch:async()=>new Response(null,{status:404})}})).status,503));
test('health rejects invalid JSON shape',async()=>assert.equal((await call(PREFIX+'/healthz',{ASSETS:{fetch:async()=>Response.json({})}})).status,503));
