# Application Security & Threat Modeling for Engineers — lesson m06l04 — Secret Scanning
# https://learnsome.tech/courses/security-course/watch?lesson=m06l04
# © LearnSome.tech
import re

patterns = {'cloud key': r'AKIA[0-9A-Z]{16}',
            'source token': r'ghp_[A-Za-z0-9]{36}'}
for number, line in enumerate(open('settings.py'), 1):
    for name, pattern in patterns.items():
        match = re.search(pattern, line)
        if match:
            value = match.group()
            print('line', number, 'HIGH', name,
                  value[:4] + '*' * 8 + value[-3:])
