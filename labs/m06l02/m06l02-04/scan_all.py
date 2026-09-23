# Application Security & Threat Modeling for Engineers — lesson m06l02 — Dynamic Scanning
# https://learnsome.tech/courses/security-course/watch?lesson=m06l02
# © LearnSome.tech
from urllib.parse import quote
from urllib.request import Request, urlopen
from harness import serve
from fixedapp import Fixed, GUARDS, STATE

PAYLOAD = '<script>steal()</script>'
server, url = serve(Fixed)
with urlopen(url + '/?q=' + quote(PAYLOAD)) as reply:
    seen, body = dict(reply.headers), reply.read().decode()
missing = [name for name in GUARDS if name not in seen]
print('headers missing:', missing or 'none')
print('payload came back unescaped:', PAYLOAD in body)
probe = Request(url + '/profile', method='POST',
                data=b'email=attacker@example.com')
try:
    urlopen(probe)
except Exception as failure:
    print('anonymous state change refused:', failure.code)
print('profile still:', STATE['email'])
server.shutdown()
