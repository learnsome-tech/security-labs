import hashlib
DB_PASSWORD = 'hunter two'
def render(request):
    return eval(request['expr'])
def fingerprint(value):
    return hashlib.md5(value.encode()).hexdigest()
