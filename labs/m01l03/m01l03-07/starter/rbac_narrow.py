RULES = [{"apiGroups": [""], "resources": ["pods"],
          "verbs": ["get", "list"]}]
ASKS = [("get", "pods"), ("get", "secrets"), ("delete", "nodes")]

def permitted(verb, resource):
    for rule in RULES:
        resources = rule["resources"]
        verbs = rule["verbs"]
        if ("*" in resources or resource in resources) and (
                "*" in verbs or verb in verbs):
            return True
    return False

for verb, resource in ASKS:
    print("ALLOW" if permitted(verb, resource) else "deny", verb, resource)
print("the same pod can no longer read one secret")
