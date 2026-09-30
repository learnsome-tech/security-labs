identities = [('root', 0), ('app', 10001)]
for name, uid in identities:
    allowed = uid != 0
    print(name, 'uid', uid, 'can bind privileged port:', not allowed)
    policy = 'application paths only' if allowed else 'all writable paths'
    print('  write policy:', policy)
accepts = any(uid == 0 for _, uid in identities[1:])
print('deployment accepts uid zero:', accepts)
