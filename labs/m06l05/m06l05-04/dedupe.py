# Application Security & Threat Modeling for Engineers — lesson m06l05 — How To Stop Drowning In Findings
# https://learnsome.tech/courses/security-course/watch?lesson=m06l05
# © LearnSome.tech
rows = [('app.py', 4, 'SEC101'), ('app.py', 4, 'SEC101'),
        ('image', 'curl', 'CVE-2023-38545'),
        ('image', 'curl', 'CVE-2023-38545')]
unique = []
for row in rows:
    if row not in unique:
        unique.append(row)
print('scanner rows:', len(rows))
print('underlying issues:', len(unique))
for row in unique:
    print('assign once:', row)
