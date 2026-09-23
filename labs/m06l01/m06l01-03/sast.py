# Application Security & Threat Modeling for Engineers — lesson m06l01 — Static Application Security Testing
# https://learnsome.tech/courses/security-course/watch?lesson=m06l01
# © LearnSome.tech
import ast

CALLS = {'eval': 'SEC101 eval on request data',
         'hashlib.md5': 'SEC104 weak hash for a token'}
found = []
tree = ast.parse(open('app.py').read())
for node in ast.walk(tree):
    if isinstance(node, ast.Call):
        who = ast.unparse(node.func)
        if who in CALLS:
            found.append((node.lineno, CALLS[who]))
    if isinstance(node, ast.Assign):
        if 'PASSWORD' in ast.unparse(node.targets[0]).upper():
            found.append((node.lineno, 'SEC103 credential in source'))
for line, rule in sorted(found):
    print('app.py', line, rule)
