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
