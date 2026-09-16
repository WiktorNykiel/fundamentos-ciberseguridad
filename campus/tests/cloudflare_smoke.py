#!/usr/bin/env python3
"""Read-only HTTP smoke test for an explicitly started local Wrangler runtime."""
import json
import time
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

BASE='http://127.0.0.1:8789'
for attempt in range(80):
    try:
        with urlopen(BASE,timeout=2) as r:
            assert r.status==200
            assert 'Fundamentos' in r.read().decode()
            assert "script-src 'self'" in r.headers.get('Content-Security-Policy','')
            assert r.headers.get('X-Content-Type-Options')=='nosniff'
        break
    except (URLError,TimeoutError):
        if attempt==79:raise
        time.sleep(.25)
with urlopen(BASE+'/course.json',timeout=5) as r:
    data=json.load(r)
    assert data['id']=='fundamentos-ciberseguridad'
    assert len(data['modules'])==32 and data['hours']==480
    assert len(data['resources'])==21
with urlopen(BASE+'/build-info.json',timeout=5) as r:
    info=json.load(r);assert info['version']=='2.2.0'
with urlopen(BASE+'/assets/catalog.js',timeout=5) as r:
    assert 'javascript' in r.headers.get('Content-Type','')
try:
    urlopen(BASE+'/not-a-real-file-123456.json',timeout=5)
    raise AssertionError('Una ruta inexistente no debe devolver éxito HTML.')
except HTTPError as e:
    assert e.code==404
print(json.dumps({'status':'passed','runtime':'wrangler-local','checks':5,'remoteDeployment':False}))
