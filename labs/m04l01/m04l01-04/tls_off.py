# Application Security & Threat Modeling for Engineers — lesson m04l01 — TLS And The Handshake
# https://learnsome.tech/courses/security-course/watch?lesson=m04l01
# © LearnSome.tech
import socket, ssl
from tlsserver import PORT

reckless = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
reckless.check_hostname = False
reckless.verify_mode = ssl.CERT_NONE

sock = socket.create_connection(("127.0.0.1", PORT))
with reckless.wrap_socket(sock, server_hostname="payments.internal") as tls:
    print("handshake completed, protocol:", tls.version())
    print("cipher suite negotiated:", tls.cipher()[0])
    print("certificate the client validated:", tls.getpeercert())
    print("encrypted, and nobody proved who they were")
