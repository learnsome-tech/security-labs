policy = {'billing-api': {'payments'}}
requests = [('billing-api', 'payments'),
            ('billing-api', 'storage'),
            ('reports-api', 'payments')]
for workload, audience in requests:
    allowed = audience in policy.get(workload, set())
    print(workload, audience, 'ACCEPT' if allowed else 'REJECT')
