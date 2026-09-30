import hashlib
import hmac

key = b'build-key-for-demo'
artefact = b'release one point four'
sig = hmac.new(key, artefact, hashlib.sha256).hexdigest()
print('signature:', sig[:20])
check = hmac.new(key, artefact, hashlib.sha256).hexdigest()
changed = hmac.new(key, b'release one point five', hashlib.sha256).hexdigest()
print('expected signer accepts release:',
      hmac.compare_digest(sig, check))
print('expected signer accepts changed bytes:',
      hmac.compare_digest(sig, changed))
print('signature covers bytes, not a version label')
