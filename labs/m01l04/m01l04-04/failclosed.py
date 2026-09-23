# Application Security & Threat Modeling for Engineers — lesson m01l04 — Secure Defaults
# https://learnsome.tech/courses/security-course/watch?lesson=m01l04
# © LearnSome.tech
POLICIES = {"/health": "public", "/orders": "owner"}

def route(path, permissive):
    policy = POLICIES.get(path)
    if policy is None:
        if permissive:
            return "served without any check"
        raise LookupError("no policy declared for " + path)
    return "served under policy " + policy

print("known route:", route("/orders", True))
print("brand new route, permissive:", route("/refunds", True))
print("brand new route, fail closed:", route("/refunds", False))
