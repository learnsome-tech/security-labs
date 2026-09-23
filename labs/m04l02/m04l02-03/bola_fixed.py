# Application Security & Threat Modeling for Engineers — lesson m04l02 — Broken Object Level Authorization
# https://learnsome.tech/courses/security-course/watch?lesson=m04l02
# © LearnSome.tech
from httplab import serve
ORDERS = {
    "1001": {"owner": "alice", "total": "310.00", "card": "4242"},
    "1002": {"owner": "bob", "total": "9.50", "card": "1881"},
}

def load_owned(caller, order_id):
    order = ORDERS.get(order_id)
    if order is None or order["owner"] != caller:
        return None
    return order

def route(caller, path):
    order = load_owned(caller, path.rsplit("/", 1)[1])
    if order is None:
        return 404, {"error": "no such order"}
    return 200, order
call = serve(route)
print("bob signs in and reads his own order, unchanged")
print(" ", call("bob", "/orders/1002"))
for guess in ["1001", "1002", "1003"]:
    print(" ", guess, call("bob", "/orders/" + guess))
