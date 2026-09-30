import hashlib

key = 'cloud-key-long-lived-demo'
print('application stores a key:', True)
print('key fingerprint:', hashlib.sha256(key.encode()).hexdigest()[:12])
print('valid after a week:', True)
print('valid after a leak:', True)
