#!/usr/bin/env python3
"""Check retained dependency-PR ancestry; read-only, requires full Git history."""
import json
import subprocess

HEADS = {
 1: '2fbb6033b8e8b111b3f00ec977ec92eda82101df',
 4: '29984f64a215c973ac89cb3d3cafba97aff3762c',
 5: '67e52b60fabe5bdc8a74646fe73ad0e59ae2ea1a',
 6: '455f5eb1a17cc36e4a8e7bc1471b3011d82c3eb2',
 10: 'dff9065670579ca08e819e4fb7f4668ac44cfae0',
 11: '282404e5cfe53bd568950872b8b9b2f7377e4930',
 12: 'e630438a5521a8908c8219e76beabcbb01e6e90a',
 13: 'e7be633ee2bce853cc516d62e37330d232b3513c',
 14: '0f8c827832ab680d762983845b42cb60e6367d85',
 15: 'e1960db7043ca083bf1456423dcc3a1e2f3c9525',
 16: '79522d540dbe23f87e84e148591d455b39456979',
}
if __name__ == '__main__':
    results = {str(pr): subprocess.run(['git','merge-base','--is-ancestor',sha,'HEAD'], check=False).returncode == 0 for pr,sha in HEADS.items()}
    print(json.dumps({'retained': results, 'allRetained': all(results.values())}, indent=2))
    raise SystemExit(0 if all(results.values()) else 1)
