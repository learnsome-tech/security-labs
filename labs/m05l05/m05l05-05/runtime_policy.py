# Application Security & Threat Modeling for Engineers — lesson m05l05 — Container Security: Minimal Bases And Non Root
# https://learnsome.tech/courses/security-course/watch?lesson=m05l05
# © LearnSome.tech
policies = [
    {'name': 'default', 'uid': 0, 'read_only': False,
     'caps': ['all']},
    {'name': 'hardened', 'uid': 10001, 'read_only': True,
     'caps': []},
]
for item in policies:
    ok = item['uid'] != 0 and item['read_only'] and not item['caps']
    print(item['name'], 'ACCEPT' if ok else 'REJECT',
          'uid', item['uid'], 'read only', item['read_only'],
          'caps', 'none' if not item['caps'] else 'all')
