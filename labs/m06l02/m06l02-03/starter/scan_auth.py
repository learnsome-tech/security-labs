from urllib.request import Request, urlopen
from harness import serve
from weakapp import Weak, STATE

server, url = serve(Weak)
print('before the probe:', STATE['email'])
probe = Request(url + '/profile', method='POST',
                data=b'email=attacker@example.com')
with urlopen(probe) as reply:
    print('no credential sent, server answered:', reply.status)
print('after the probe:', STATE['email'])
print('state changed with no credential:',
      STATE['email'] != 'owner@example.com')
server.shutdown()
