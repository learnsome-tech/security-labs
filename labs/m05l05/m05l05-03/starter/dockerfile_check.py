def inspect(text):
    lines = [line.strip() for line in text.splitlines()]
    user = next((line for line in lines if line.startswith('USER ')), None)
    base = next((line for line in lines if line.startswith('FROM ')), '')
    return base, user

unsafe = 'FROM python:3.14\nCOPY app.py /app.py\nCMD python app.py'
safer = ('FROM python:3.14-slim\nUSER app\n'
         'COPY app.py /app.py\nCMD python app.py')
for name, text in [('unsafe', unsafe), ('safer', safer)]:
    base, user = inspect(text)
    print(name, 'base:', base[5:], 'explicit user:', user is not None)
    verdict = 'REJECT root default' if user is None else 'OK non root declared'
    print('  verdict:', verdict)
