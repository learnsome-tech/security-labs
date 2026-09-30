commits = [('add settings', 'TOKEN = ghp_demo'),
           ('move to environment', 'TOKEN = os.environ[APP_TOKEN]')]
print('working tree scan: clean')
for subject, content in commits:
    print(subject, 'contains token:', 'ghp_' in content)
