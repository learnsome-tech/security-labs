# Application Security & Threat Modeling for Engineers — lesson m01l01 — The Threat Model Habit
# https://learnsome.tech/courses/security-course/watch?lesson=m01l01
# © LearnSome.tech
ROUTES = [
    ("GET", "/health", False, False),
    ("POST", "/orders", True, True),
    ("POST", "/internal/refund", False, True),
    ("GET", "/orders/{id}", True, False),
]

for method, path, authenticated, changes_state in ROUTES:
    risk = changes_state and not authenticated
    print(method, path, "auth" if authenticated else "anonymous",
          "FINDING" if risk else "ok")
print("routes:", len(ROUTES))
print("anonymous and state changing:",
      sum(1 for r in ROUTES if r[3] and not r[2]))
