from vault import Vault

POLICY = {"billing": ("stripe-key",)}
vault = Vault(POLICY)
vault.put("stripe-key", "sk-live-old-aaaa")

def upstream(value):
    current = vault.versions["stripe-key"][-1]
    return "accepted" if value == current else "rejected"

first = vault.get("stripe-key", caller="billing").reveal()
print("version one at the upstream:", upstream(first))

print("rotation stores version:", vault.put("stripe-key", "sk-live-new-bbbb"))
second = vault.get("stripe-key", caller="billing")
print("current version is now:", second.version)
print("version two at the upstream:", upstream(second.reveal()))
print("version one at the upstream:", upstream(first))
