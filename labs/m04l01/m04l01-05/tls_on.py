# Application Security & Threat Modeling for Engineers — lesson m04l01 — TLS And The Handshake
# https://learnsome.tech/courses/security-course/watch?lesson=m04l01
# © LearnSome.tech
import socket, ssl
from tlsserver import PORT

def attempt(name, authority):
    ctx = ssl.create_default_context(cafile=authority)
    sock = socket.create_connection(("127.0.0.1", PORT))
    try:
        with ctx.wrap_socket(sock, server_hostname=name) as tls:
            print("connected as", name, "over", tls.version())
    except ssl.SSLCertVerificationError as err:
        print(type(err).__name__, "asking for", name)
        print(" ", err.reason, "-", err.verify_message)

attempt("payments.internal", "ca.pem")
attempt("orders.internal", None)
attempt("orders.internal", "ca.pem")
