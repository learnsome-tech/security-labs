import hashlib, socket, ssl
from tlsserver import PORT

def pin(der_bytes):
    return hashlib.sha256(der_bytes).hexdigest()

with open("srv.pem") as handle:
    shipped = pin(ssl.PEM_cert_to_DER_cert(handle.read()))

ctx = ssl.create_default_context(cafile="ca.pem")
sock = socket.create_connection(("127.0.0.1", PORT))
with ctx.wrap_socket(sock, server_hostname="orders.internal") as tls:
    seen = pin(tls.getpeercert(True))

print("authority vouched for the name:", True)
print("pin shipped with the client matches:", seen == shipped)
print("pin from last year matches:", seen == pin(b"an older certificate"))
print("pinning trades one outage risk for one attack")
