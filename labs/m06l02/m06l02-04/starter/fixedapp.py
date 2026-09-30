from html import escape
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
STATE = {'email': 'owner@example.com'}
GUARDS = {'Content-Security-Policy': "default-src 'self'", 'X-Content-Type-Options': 'nosniff', 'X-Frame-Options': 'DENY', 'Strict-Transport-Security': 'max-age=63072000'}
class Fixed(BaseHTTPRequestHandler):
    def log_message(self, *args): pass
    def reply(self, code, body=''):
        self.send_response(code)
        for name, value in GUARDS.items(): self.send_header(name, value)
        self.end_headers(); self.wfile.write(body.encode())
    def do_GET(self):
        term = parse_qs(urlparse(self.path).query).get('q', [''])[0]
        self.reply(200, '<p>you searched for ' + escape(term) + '</p>')
    def do_POST(self):
        if self.headers.get('Authorization') != 'Bearer owner-token': return self.reply(401)
        self.reply(204)
