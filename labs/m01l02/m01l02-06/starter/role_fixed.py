import json

ROLES = {"alice": "admin", "bob": "viewer"}

def handle(request_body):
    claims = json.loads(request_body)
    user = claims["user"]
    role = ROLES.get(user, "none")
    if role == "admin":
        return user + " deleted the customer table"
    return user + " may not do that, role is " + role

print(handle('{"user": "bob", "role": "viewer"}'))
print(handle('{"user": "bob", "role": "admin"}'))
print(handle('{"user": "alice", "role": "viewer"}'))
