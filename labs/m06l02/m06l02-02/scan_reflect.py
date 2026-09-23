# Application Security & Threat Modeling for Engineers — lesson m06l02 — Dynamic Scanning
# https://learnsome.tech/courses/security-course/watch?lesson=m06l02
# © LearnSome.tech
from urllib.parse import quote
from urllib.request import urlopen
from harness import serve
from weakapp import Weak

PAYLOAD = '<script>steal()</script>'
server, url = serve(Weak)
with urlopen(url + '/?q=' + quote(PAYLOAD)) as reply:
    body = reply.read().decode()
print('probe sent:', PAYLOAD)
print('page body:', body)
print('payload came back unescaped:', PAYLOAD in body)
server.shutdown()
