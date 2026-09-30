from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
STATE = {'email': 'owner@example.com'}
class Weak(BaseHTTPRequestHandler):
    def log_message(self, *args): pass
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        form = parse_qs(self.rfile.read(length).decode())
        STATE['email'] = form['email'][0]
        self.send_response(204)
        self.end_headers()
