baseline = {'SEC101 old eval', 'CVE old package'}
current = ['SEC101 old eval', 'CVE old package',
           'SEC104 new weak hash', 'SECRET new token']
new = [item for item in current if item not in baseline]
print('baseline findings:', len(baseline))
print('new findings:', len(new))
for item in new:
    print('FAIL new:', item)
print('change accepted:', not new)
