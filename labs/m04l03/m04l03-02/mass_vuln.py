# Application Security & Threat Modeling for Engineers — lesson m04l03 — Mass Assignment
# https://learnsome.tech/courses/security-course/watch?lesson=m04l03
# © LearnSome.tech
from apilab import serve
USERS = {}

def create(caller, body):
    user = {"name": "", "role": "customer", "balance": 0}
    user.update(body)
    USERS[user["name"]] = user
    return 201, user

post = serve(create)
print("the documented signup request:")
print(" ", post("signup", {"name": "mallory"}))
print("the same endpoint, with two fields nobody wrote down:")
print(" ", post("signup", {"name": "mallory", "role": "admin",
                           "balance": 9999}))
