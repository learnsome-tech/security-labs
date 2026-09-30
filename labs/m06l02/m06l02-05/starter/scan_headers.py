from urllib.request import urlopen
from harness import serve
from weakapp import Weak

WANTED = ['Content-Security-Policy', 'X-Content-Type-Options',
          'X-Frame-Options', 'Strict-Transport-Security']
server, url = serve(Weak)
with urlopen(url + '/?q=hello') as reply:
    seen = dict(reply.headers)
for name in WANTED:
    print('present' if name in seen else 'MISSING', name)
print('banner names the stack:', 'Python' in seen.get('Server', ''))
server.shutdown()
