class Config:
    def __init__(self, host, token):
        self.host = host
        self.token = token

cfg = Config("api.example.com", "sk-live-4d1f-demo")

try:
    raise TimeoutError("upstream did not answer")
except TimeoutError as err:
    print("request failed:", err)
    print("context:", vars(cfg))
