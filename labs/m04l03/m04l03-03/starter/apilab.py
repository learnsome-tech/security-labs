import json, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def serve(route):
    """Run `route` behind a real local HTTP server and return a caller."""

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_POST(self):
            length = int(self.headers.get("Content-Length", "0"))
            sent = json.loads(self.rfile.read(length) or b"{}")
            caller = self.headers.get("X-User", "anonymous")
            status, result = route(caller, sent)
            body = json.dumps(result, sort_keys=True).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = "http://127.0.0.1:" + str(server.server_address[1])

    def post(caller, payload):
        request = Request(base + "/users",
                          data=json.dumps(payload).encode(),
                          headers={"X-User": caller,
                                   "Content-Type": "application/json"})
        try:
            with urlopen(request) as response:
                return response.status, json.load(response)
        except HTTPError as error:
            return error.code, json.load(error)

    return post
