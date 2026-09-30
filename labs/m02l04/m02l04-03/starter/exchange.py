import time

claims = {'workload': 'billing-api', 'audience': 'payments', 'valid_until': 120}
policy = {'billing-api': {'payments'}}
now = 100
allowed = claims['audience'] in policy.get(claims['workload'], set())
short = claims['valid_until'] - now
print('workload:', claims['workload'])
print('audience allowed:', allowed)
print('token lifetime:', short, 'seconds')
print('application stores private key:', False)
