# Application Security & Threat Modeling for Engineers — lesson m06l03 — Image Scanning And Trivy
# https://learnsome.tech/courses/security-course/watch?lesson=m06l03
# © LearnSome.tech
from scan import findings
RANK = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2}
hits = sorted(findings('app:debian'), key=lambda h: RANK[h[0]['severity']])
for adv, pkg in hits:
    fix = 'fix in ' + adv['fixed'] if adv['fixed'] else 'NO FIX PUBLISHED'
    print(adv['severity'], adv['id'], pkg['name'], pkg['version'], fix)
