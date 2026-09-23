# Application Security & Threat Modeling for Engineers — lesson m06l01 — Static Application Security Testing
# https://learnsome.tech/courses/security-course/watch?lesson=m06l01
# © LearnSome.tech
import ast

source = 'request.args.get'
sink = 'os.system'
for fn in ast.parse(open('taint_app.py').read()).body:
    if not isinstance(fn, ast.FunctionDef):
        continue
    tainted = set()
    for node in ast.walk(fn):
        if isinstance(node, ast.Assign):
            text = ast.unparse(node.value)
            names = {n.id for n in ast.walk(node.value)
                     if isinstance(n, ast.Name)}
            if source in text or names & tainted:
                tainted.add(node.targets[0].id)
        if isinstance(node, ast.Call) and ast.unparse(node.func) == sink:
            names = {n.id for n in ast.walk(node)
                     if isinstance(n, ast.Name)} & tainted
            print(fn.name, 'TAINTED via', ', '.join(sorted(names)))
