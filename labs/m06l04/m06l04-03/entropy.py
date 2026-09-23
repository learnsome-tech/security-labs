# Application Security & Threat Modeling for Engineers — lesson m06l04 — Secret Scanning
# https://learnsome.tech/courses/security-course/watch?lesson=m06l04
# © LearnSome.tech
import math

def entropy(text):
    counts = [text.count(c) / len(text) for c in set(text)]
    return -sum(p * math.log2(p) for p in counts)

samples = [('token', '9fK2mQ7xR4tV8bN1cJ6hL0sD3wY5zA7eG2pU'),
           ('comment', 'the quick brown fox jumps over it'),
           ('digest', '9f86d081884c7d659a2feaa0c55ad015')]
for label, text in samples:
    verdict = 'flagged' if entropy(text) > 3.6 else 'ignored'
    print(label, verdict)
