# Application Security & Threat Modeling for Engineers — lesson m02l03 — Moving To A Secret Manager
# https://learnsome.tech/courses/security-course/watch?lesson=m02l03
# © LearnSome.tech
from vault import Vault

POLICY = {"billing": ("stripe-key",), "reports": ()}

vault = Vault(POLICY)
vault.put("stripe-key", "sk-live-4d1f-demo")

lease = vault.get("stripe-key", caller="billing")
print("billing receives:", lease)
print("value ends with:", lease.reveal()[-4:])

try:
    vault.get("stripe-key", caller="reports")
except PermissionError as err:
    print("refused:", err)

print("audit trail:")
for caller, name, verdict in vault.audit:
    print(" -", caller, name, verdict)
