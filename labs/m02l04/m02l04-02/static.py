# Application Security & Threat Modeling for Engineers — lesson m02l04 — Workload Identity
# https://learnsome.tech/courses/security-course/watch?lesson=m02l04
# © LearnSome.tech
import hashlib

key = 'cloud-key-long-lived-demo'
print('application stores a key:', True)
print('key fingerprint:', hashlib.sha256(key.encode()).hexdigest()[:12])
print('valid after a week:', True)
print('valid after a leak:', True)
