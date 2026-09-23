# Application Security & Threat Modeling for Engineers — lesson m06l02 — Dynamic Scanning
# https://learnsome.tech/courses/security-course/watch?lesson=m06l02
# © LearnSome.tech
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
class Weak(BaseHTTPRequestHandler):
    def log_message(self, *args): pass
    def do_GET(self):
        term = parse_qs(urlparse(self.path).query).get('q', [''])[0]
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(('<p>you searched for ' + term + '</p>').encode())
