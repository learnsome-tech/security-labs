# Application Security & Threat Modeling for Engineers — lesson m06l03 — Image Scanning And Trivy
# https://learnsome.tech/courses/security-course/watch?lesson=m06l03
# © LearnSome.tech
import json
INVENTORY = json.load(open('inventory.json'))['images']
ADVISORIES = json.load(open('advisories.json'))
def older(have, fixed):
    return tuple(int(n) for n in have.split('.')) < tuple(int(n) for n in fixed.split('.'))
def findings(image):
    hits = []
    for pkg in INVENTORY[image]['packages']:
        for adv in ADVISORIES:
            if adv['package'] == pkg['name'] and (not adv['fixed'] or older(pkg['version'], adv['fixed'])): hits.append((adv, pkg))
    return hits
