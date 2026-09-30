import hashlib

original = b'release one point four'
recorded = hashlib.sha256(original).hexdigest()
print('recorded digest:', recorded[:16])
copies = [('release copy', original),
          ('tampered copy', b'release one point five')]
for label, data in copies:
    actual = hashlib.sha256(data).hexdigest()
    print(label, 'matches:', actual == recorded)
print('the digest identifies bytes, not the author')
