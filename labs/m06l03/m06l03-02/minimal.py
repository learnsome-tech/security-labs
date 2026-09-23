# Application Security & Threat Modeling for Engineers — lesson m06l03 — Image Scanning And Trivy
# https://learnsome.tech/courses/security-course/watch?lesson=m06l03
# © LearnSome.tech
from scan import INVENTORY, findings

for image in ('app:debian', 'app:alpine'):
    hits = findings(image)
    base = sum(1 for adv, pkg in hits if pkg['layer'] == 'base')
    print(image, 'built on', INVENTORY[image]['base'])
    print('   packages:', len(INVENTORY[image]['packages']),
          'findings:', len(hits), 'in the base:', base)
print('your own dependencies survived the swap untouched')
