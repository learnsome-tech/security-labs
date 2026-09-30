from httplab import serve

CUSTOMERS = {"c-7": "bob", "c-9": "alice"}
ORDERS = {
    "1001": {"customer": "c-9", "total": "310.00"},
    "1002": {"customer": "c-7", "total": "9.50"},
}

def route(caller, path):
    _, _, customer, _, order_id = path.split("/")
    if CUSTOMERS.get(customer) != caller:
        return 403, {"error": "not your account"}
    order = ORDERS.get(order_id)
    if order is None:
        return 404, {"error": "no such order"}
    return 200, order

call = serve(route)
print("his own account, his own order")
print(" ", call("bob", "/customers/c-7/orders/1002"))
print("his own account, somebody else's order")
print(" ", call("bob", "/customers/c-7/orders/1001"))
