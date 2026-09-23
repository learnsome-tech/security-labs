# Application Security & Threat Modeling for Engineers — lesson m04l01 — TLS And The Handshake
# https://learnsome.tech/courses/security-course/watch?lesson=m04l01
# © LearnSome.tech
import socket, ssl, subprocess, threading

subprocess.run(["bash", "mkcert.sh"], check=True)
CTX = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
CTX.load_cert_chain("srv.pem", "srv.key")
LISTENER = socket.create_server(("127.0.0.1", 0))
PORT = LISTENER.getsockname()[1]

def _serve():
    while True:
        raw, _ = LISTENER.accept()
        try:
            CTX.wrap_socket(raw, server_side=True).close()
        except OSError:
            raw.close()

threading.Thread(target=_serve, daemon=True).start()
