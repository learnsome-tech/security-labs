import json

def handle(request_body):
    claims = json.loads(request_body)
    user = claims["user"]
    role = claims["role"]
    if role == "admin":
        return user + " deleted the customer table"
    return user + " may not do that"

print(handle('{"user": "bob", "role": "viewer"}'))
print(handle('{"user": "bob", "role": "admin"}'))
