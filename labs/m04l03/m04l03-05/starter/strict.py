from apilab import serve
WRITABLE = {"name", "email"}

def create(caller, body):
    unknown = sorted(set(body) - WRITABLE)
    if unknown:
        return 400, {"error": "unknown fields rejected",
                     "fields": unknown}
    user = {"name": "", "email": "", "role": "customer", "balance": 0}
    user.update(body)
    return 201, user

post = serve(create)
print("a clean request, only documented fields:")
print(" ", post("mallory", {"name": "mallory", "email": "m@x.io"}))
print("the same attack, now answered rather than absorbed:")
print(" ", post("mallory", {"name": "mallory", "role": "admin",
                            "balance": 9999}))
