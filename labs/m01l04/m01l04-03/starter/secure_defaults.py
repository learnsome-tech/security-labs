DEFAULTS = {
    "debug": False,
    "verify_tls": True,
    "allowed_origins": [],
    "cookie_secure": True,
}
UNSAFE_IN_PRODUCTION = {"debug": True, "verify_tls": False}

def start(env, overrides):
    config = dict(DEFAULTS)
    config.update(overrides)
    for key, danger in UNSAFE_IN_PRODUCTION.items():
        if env == "production" and config[key] == danger:
            raise ValueError("refusing to start: " + key + " is unsafe here")
    return config

laptop = start("laptop", {"verify_tls": False})
print("laptop, tls check off:", laptop["verify_tls"])
print(start("production", {"verify_tls": False}))
