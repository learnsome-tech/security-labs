from datetime import date

items = [('legacy tls finding', date(2026, 9, 20), 'platform'),
         ('temporary package risk', date(2026, 9, 10), 'service')]
today = date(2026, 9, 11)
for title, until, owner in items:
    state = 'ACTIVE' if until >= today else 'EXPIRED'
    print(state, title, 'owner:', owner, 'until:', until.isoformat())
