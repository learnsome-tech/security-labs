# Application Security & Threat Modeling for Engineers — lesson m01l02 — Authentication Versus Authorisation
# https://learnsome.tech/courses/security-course/watch?lesson=m01l02
# © LearnSome.tech
import hashlib, hmac, os

def store(password):
    salt = os.urandom(16)
    key = hashlib.scrypt(password.encode(), salt=salt, n=16384, r=8, p=1)
    return salt, key

def verify(password, salt, key):
    candidate = hashlib.scrypt(password.encode(), salt=salt, n=16384,
                               r=8, p=1)
    return hmac.compare_digest(candidate, key)

salt, key = store("correct horse battery staple")
print("stored key length in bytes:", len(key))
print("right password:", verify("correct horse battery staple", salt, key))
print("wrong password:", verify("Correct Horse Battery Staple", salt, key))
print("authentication answers who you are, and nothing else")
