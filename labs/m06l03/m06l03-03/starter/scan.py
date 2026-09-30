import json
INVENTORY = json.load(open('inventory.json'))['images']
ADVISORIES = json.load(open('advisories.json'))
def older(have, fixed): return tuple(map(int, have.split('.'))) < tuple(map(int, fixed.split('.')))
def findings(image): return [(a,p) for p in INVENTORY[image]['packages'] for a in ADVISORIES if a['package'] == p['name'] and (not a['fixed'] or older(p['version'], a['fixed']))]
