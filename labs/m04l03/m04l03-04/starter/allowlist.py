from apilab import serve
WRITABLE = {"create": {"name", "email"}, "update": {"email"}}
USERS = {}

def handle(caller, body):
    operation = body.pop("operation")
    user = USERS.setdefault(caller, {"name": "", "email": "",
                                     "role": "customer", "balance": 0})
    for field in sorted(WRITABLE[operation]):
        if field in body:
            user[field] = body[field]
    return 200, user

post = serve(handle)
print("create, with the promotion attempt attached:")
print(" ", post("mallory", {"operation": "create", "name": "mallory",
                            "role": "admin", "balance": 9999}))
print("update, where even the name is not writable:")
print(" ", post("mallory", {"operation": "update", "name": "admin",
                            "email": "m@x.io"}))
