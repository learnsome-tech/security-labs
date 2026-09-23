# Application Security & Threat Modeling for Engineers — lesson m06l02 — Dynamic Scanning
# https://learnsome.tech/courses/security-course/watch?lesson=m06l02
# © LearnSome.tech
import threading
from http.server import ThreadingHTTPServer
def serve(handler):
    server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, 'http://127.0.0.1:' + str(server.server_address[1])
