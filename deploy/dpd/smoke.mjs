/** Public GET/HEAD checks. Does not change routes, DNS or deploy anything. */
import assert from 'node:assert/strict';
const target = new URL(process.argv[2] || 'https://smartkea.com');
if (!['http:', 'https:'].includes(target.protocol) || target.username || target.password || target.pathname !== '/') throw new Error('Supply an origin without a path or credentials');
const base = '/introduccion-dpd';
for (const [path, status, type] of [[base, 308, null], [base+'?probe=1', 308, null], [base+'/', 200, 'text/html'], [base+'/healthz', 200, 'application/json'], [base+'/missing-asset.js',404,null]]) {
  const res = await fetch(new URL(path,target), {redirect:'manual', signal:AbortSignal.timeout(15000)});
  assert.equal(res.status,status,`Status for ${path}`);
  if (status===308) {
    const next=new URL(res.headers.get('location'),target);
    assert.equal(next.origin,target.origin);assert.equal(next.pathname,base+'/');
    assert.equal(next.search,new URL(path,target).search);
  }
  if (type) assert.ok(res.headers.get('content-type')?.includes(type),`MIME for ${path}`);
  if (status!==308) for (const h of ['content-security-policy','x-content-type-options','referrer-policy']) assert.ok(res.headers.has(h),h);
  assert.equal(res.headers.get('set-cookie'),null);
  if (path===base+'/healthz') {
    const body=await res.json(); assert.equal(body.application,'introduccion-dpd');
    assert.match(body.treeSha256,/^[a-f0-9]{64}$/);
    if (process.env.EXPECTED_COMMIT) assert.equal(body.sourceCommit,process.env.EXPECTED_COMMIT);
  }
  console.log(JSON.stringify({path,status:res.status,passed:true}));
}
const head=await fetch(new URL(base+'/',target),{method:'HEAD',redirect:'manual',signal:AbortSignal.timeout(15000)});
assert.equal(head.status,200); assert.equal((await head.arrayBuffer()).byteLength,0);
console.log('Smoke checks passed. Separately compare root/other routes with the pre-deploy baseline.');
