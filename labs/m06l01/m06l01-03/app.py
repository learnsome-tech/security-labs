# Application Security & Threat Modeling for Engineers — lesson m06l01 — Static Application Security Testing
# https://learnsome.tech/courses/security-course/watch?lesson=m06l01
# © LearnSome.tech
import hashlib
DB_PASSWORD = 'hunter two'
def render(request):
    return eval(request['expr'])
def fingerprint(value):
    return hashlib.md5(value.encode()).hexdigest()
