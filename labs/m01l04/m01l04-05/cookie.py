# Application Security & Threat Modeling for Engineers — lesson m01l04 — Secure Defaults
# https://learnsome.tech/courses/security-course/watch?lesson=m01l04
# © LearnSome.tech
def set_cookie(name, value, **options):
    flags = {"Secure": True, "HttpOnly": True, "SameSite": "Lax",
             "Path": "/"}
    flags.update(options)
    parts = [name + "=" + value]
    for key, setting in flags.items():
        if setting is True:
            parts.append(key)
        elif setting:
            parts.append(key + "=" + str(setting))
    return "Set-Cookie: " + "; ".join(parts)

print(set_cookie("session", "abc123"))
print(set_cookie("session", "abc123", HttpOnly=False, SameSite="None"))
