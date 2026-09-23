# Application Security & Threat Modeling for Engineers — lesson m02l04 — Workload Identity
# https://learnsome.tech/courses/security-course/watch?lesson=m02l04
# © LearnSome.tech
tokens = [('fresh', 100, 120), ('old', 100, 90)]
now = 100
for name, issued, expires in tokens:
    valid = now < expires
    print(name, 'accepted' if valid else 'REJECTED',
          'remaining:', max(0, expires - now), 'seconds')
now = 121
print('fresh token after time advances:', now < tokens[0][2])
