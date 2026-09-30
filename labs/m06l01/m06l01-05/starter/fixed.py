import ast

source = 'request.args.get'
sink = 'subprocess.run'
for fn in ast.parse(open('fixed_app.py').read()).body:
    if not isinstance(fn, ast.FunctionDef):
        continue
    for node in ast.walk(fn):
        if isinstance(node, ast.Call) and ast.unparse(node.func) == sink:
            shell = any(k.arg == 'shell' and getattr(k.value, 'value', False)
                        for k in node.keywords)
            print(fn.name, 'shell mode:', shell, 'list arguments:',
                  isinstance(node.args[0], (ast.List, ast.Tuple)))
