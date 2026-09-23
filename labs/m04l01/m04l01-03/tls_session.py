# Application Security & Threat Modeling for Engineers — lesson m04l01 — TLS And The Handshake
# https://learnsome.tech/courses/security-course/watch?lesson=m04l01
# © LearnSome.tech
import socket, ssl, subprocess, threading
subprocess.run(["bash", "mkcert.sh"], check=True)

server_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
server_ctx.load_cert_chain("srv.pem", "srv.key")
listener = socket.create_server(("127.0.0.1", 0))
port = listener.getsockname()[1]

def serve():
    raw, _ = listener.accept()
    with server_ctx.wrap_socket(raw, server_side=True) as tls:
        tls.sendall(b"hello from the orders service")

threading.Thread(target=serve, daemon=True).start()
trust = ssl.create_default_context(cafile="ca.pem")
plain = socket.create_connection(("127.0.0.1", port))
with trust.wrap_socket(plain, server_hostname="orders.internal") as tls:
    print("negotiated protocol:", tls.version())
    print("cipher suite:", tls.cipher()[0])
    print("peer subject:", tls.getpeercert()["subject"][0][0])
    print("server said:", tls.recv(64).decode())
