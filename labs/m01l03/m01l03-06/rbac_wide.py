# Application Security & Threat Modeling for Engineers — lesson m01l03 — Least Privilege In IAM And RBAC
# https://learnsome.tech/courses/security-course/watch?lesson=m01l03
# © LearnSome.tech
RULES = [{"apiGroups": [""], "resources": ["*"], "verbs": ["*"]}]
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
print("a pod with this role can read every service account token")
