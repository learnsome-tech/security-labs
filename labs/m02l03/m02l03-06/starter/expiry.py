import time
from vault import Vault
from lease import Expired

vault = Vault({"billing": ("stripe-key",)})
vault.put("stripe-key", "sk-live-4d1f-demo")
cache = {}

def token():
    held = cache.get("lease")
    if held is None or not held.valid():
        cache["lease"] = vault.get("stripe-key", "billing", ttl=1)
    return cache["lease"].reveal()

print("first call:", token()[-4:], "fetches:", len(vault.audit))
print("second call:", token()[-4:], "fetches:", len(vault.audit))
time.sleep(1.2)
print("after the lease ends:", token()[-4:], "fetches:", len(vault.audit))
try:
    vault.get("stripe-key", "billing", ttl=0).reveal()
except Expired as err:
    print("refused:", err)
