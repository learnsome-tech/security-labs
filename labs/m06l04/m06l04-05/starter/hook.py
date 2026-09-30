import re

pattern = re.compile(r'ghp_[A-Za-z0-9]{36}|AKIA[0-9A-Z]{16}')
changes = [('new token', 'TOKEN = ghp_9fK2mQ7xR4tV8bN1cJ6hL0sD3wY5zA7eG2pU'),
           ('environment lookup', 'TOKEN = os.environ[APP_TOKEN]')]
for name, text in changes:
    print(name, 'rejected' if pattern.search(text) else 'accepted')
