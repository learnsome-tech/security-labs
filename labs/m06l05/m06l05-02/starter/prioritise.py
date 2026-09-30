findings = [
    ('critical', True, True, 'public api injection'),
    ('high', False, True, 'unused image package'),
    ('medium', True, False, 'known library issue'),
    ('high', True, True, 'secret in build log')]
rank = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
ordered = sorted(findings, key=lambda x: (rank[x[0]], not x[1], not x[2]))
for severity, reachable, fix, title in ordered:
    print(severity.upper(), 'reachable' if reachable else 'unreachable',
          'fix' if fix else 'no fix', '-', title)
