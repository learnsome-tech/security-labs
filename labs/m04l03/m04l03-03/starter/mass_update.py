from apilab import serve
ORDERS = {"1002": {"owner_id": "u-bob", "status": "pending",
                   "refunded": False}}

def update(caller, body):
    order = ORDERS[body.pop("id")]
    order.update(body)
    return 200, order

post = serve(update)
print("the documented update adds a delivery note:")
print(" ", post("bob", {"id": "1002", "note": "back door"}))
print("the undocumented update rewrites state and ownership:")
print(" ", post("bob", {"id": "1002", "status": "paid",
                        "refunded": True, "owner_id": "u-mallory"}))
