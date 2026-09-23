# Application Security & Threat Modeling for Engineers — lesson m01l04 — Secure Defaults
# https://learnsome.tech/courses/security-course/watch?lesson=m01l04
# © LearnSome.tech
DEFAULTS = {
    "debug": True,
    "verify_tls": False,
    "allowed_origins": "*",
    "cookie_secure": False,
    "admin_password": "changeme",
}

def start(env, overrides):
    config = dict(DEFAULTS)
    config.update(overrides)
    print("starting in", env)
    for key, value in config.items():
        print(" ", key, "=", value)
    return config

start("production", {})
print("nobody typed anything wrong, and every setting is unsafe")
