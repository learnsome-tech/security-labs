import secrets
from httplab import serve
ORDERS = {secrets.token_urlsafe(12): {"owner": name}
          for name in ["alice", "bob"]}

def route(caller, path):
    order = ORDERS.get(path.rsplit("/", 1)[1])
    if order is None:
        return 404, {"error": "no such order"}
    return 200, order

call = serve(route)
found = 0
for guess in range(400):
    status, _ = call("bob", "/orders/" + str(1000 + guess))
    found += status == 200
print("sequential identifiers tried:", 400)
print("orders discovered by guessing:", found)
leaked = [k for k, v in ORDERS.items() if v["owner"] == "alice"][0]
print("now one identifier leaks through a referer header")
print(" ", call("bob", "/orders/" + leaked))
print("random identifiers hide the door; they do not lock it")
