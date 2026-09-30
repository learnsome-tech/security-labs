import time
from lease import Lease

class Vault:
    def __init__(self, policy):
        self.policy = policy
        self.versions = {}
        self.audit = []

    def put(self, name, value):
        chain = self.versions.setdefault(name, [])
        chain.append(value)
        return len(chain)

    def get(self, name, caller, ttl=30):
        ok = name in self.policy.get(caller, ())
        self.audit.append((caller, name, "granted" if ok else "denied"))
        if not ok:
            raise PermissionError(caller + " may not read " + name)
        chain = self.versions[name]
        return Lease(chain[-1], len(chain), time.time() + ttl)
