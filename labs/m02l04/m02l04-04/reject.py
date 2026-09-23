# Application Security & Threat Modeling for Engineers — lesson m02l04 — Workload Identity
# https://learnsome.tech/courses/security-course/watch?lesson=m02l04
# © LearnSome.tech
policy = {'billing-api': {'payments'}}
requests = [('billing-api', 'payments'),
            ('billing-api', 'storage'),
            ('reports-api', 'payments')]
for workload, audience in requests:
    allowed = audience in policy.get(workload, set())
    print(workload, audience, 'ACCEPT' if allowed else 'REJECT')
