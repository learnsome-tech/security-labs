class Secret:
    def __init__(self, value):
        self._value = value
    def reveal(self):
        return self._value
    def __repr__(self):
        return "Secret(ending " + self._value[-4:] + ")"
    __str__ = __repr__

class Config:
    def __init__(self, host, token):
        self.host = host
        self.token = Secret(token)

cfg = Config("api.example.com", "sk-live-4d1f-demo")

try:
    raise TimeoutError("upstream did not answer")
except TimeoutError as err:
    print("request failed:", err)
    print("context:", vars(cfg))
print("still usable:", len(cfg.token.reveal()), "characters")
