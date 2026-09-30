import hashlib
import json

source = b'commit seven seven seven'
prov = {"source": "repo@example/checkout",
        "revision": "777", "builder": "ci trusted pool",
        "source_digest": hashlib.sha256(source).hexdigest()}
print('source:', prov['source'], 'revision', prov['revision'])
print('builder:', prov['builder'])
print('source digest recorded:', prov['source_digest'][:16])
received = json.loads(json.dumps(prov))
print('policy accepts builder:', received['builder'] == 'ci trusted pool')
print('policy accepts revision:', received['revision'] == '777')
