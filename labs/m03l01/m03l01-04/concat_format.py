# Application Security & Threat Modeling for Engineers — lesson m03l01 — Injection In All Its Forms
# https://learnsome.tech/courses/security-course/watch?lesson=m03l01
# © LearnSome.tech
SECRET = "deploy-key-4417"

class User:
    def __init__(self, name):
        self.name = name
        self.session = "s-9001"

def render(template, user):
    return template.format(u=user)

bob = User("bob")
print(render("Hello {u.name}", bob))
print(render("Hello {u.name}, session {u.session}", bob))
print(render("Hello {u.__init__.__globals__[SECRET]}", bob))
