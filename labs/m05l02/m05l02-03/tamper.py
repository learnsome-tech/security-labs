# Application Security & Threat Modeling for Engineers — lesson m05l02 — Lockfiles And Reproducible Builds
# https://learnsome.tech/courses/security-course/watch?lesson=m05l02
# © LearnSome.tech
import hashlib

with open("wheel.bin", "rb") as handle:
    original = handle.read()

locked = hashlib.sha256(original).hexdigest()
print("bytes we asked for:", len(original))
print("digest in the lock:", locked[:32])

altered = bytearray(original)
altered[7] ^= 1
print("one bit flipped in one byte, nothing else changed")

served = hashlib.sha256(bytes(altered)).hexdigest()
print("digest of what arrived:", served[:32])
print("same length:", len(altered) == len(original))
print("verdict:", "match" if served == locked else "REJECT the artefact")
