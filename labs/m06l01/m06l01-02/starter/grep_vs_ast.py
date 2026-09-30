import ast
import re

source = open('sample.py').read()
for n, text in enumerate(source.splitlines(), 1):
    if re.search(r'eval\(.*\)', text):
        print('regex hit on line', n)
print('tree pass')
for node in ast.walk(ast.parse(source)):
    if isinstance(node, ast.Call) and ast.unparse(node.func) == 'eval':
        print('real call to eval on line', node.lineno)
