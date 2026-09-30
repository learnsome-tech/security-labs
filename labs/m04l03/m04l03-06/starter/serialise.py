from apilab import serve
RECORD = {"name": "alice", "email": "alice@example.com",
          "role": "admin", "password_hash": "scrypt:16384:8:1",
          "fraud_score": 0.82, "internal_note": "under review"}
PUBLIC = ("name", "role")

def show(caller, body):
    if body.get("style") == "whole model":
        return 200, RECORD
    return 200, {field: RECORD[field] for field in PUBLIC}

post = serve(show)
for style in ["whole model", "serialiser"]:
    status, payload = post("mallory", {"style": style})
    print("fields the client receives from the", style + ":")
    for field in sorted(payload):
        print("  -", field)
