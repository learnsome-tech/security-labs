# Application Security & Threat Modeling for Engineers — lesson m01l02 — Authentication Versus Authorisation
# https://learnsome.tech/courses/security-course/watch?lesson=m01l02
# © LearnSome.tech
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
