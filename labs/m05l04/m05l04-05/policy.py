# Application Security & Threat Modeling for Engineers — lesson m05l04 — Provenance And Signing
# https://learnsome.tech/courses/security-course/watch?lesson=m05l04
# © LearnSome.tech
records = [
    {'name': 'release one', 'builder': 'ci trusted pool',
     'signed': True},
    {'name': 'release two', 'builder': 'laptop shell', 'signed': True},
    {'name': 'release three', 'builder': 'ci trusted pool',
     'signed': False},
]
for item in records:
    accepted = item['signed'] and item['builder'] == 'ci trusted pool'
    verdict = 'ACCEPT' if accepted else 'REJECT'
    print(item['name'], verdict, '-', item['builder'])
