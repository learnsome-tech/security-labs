# Application Security & Threat Modeling for Engineers — lesson m02l01 — Why Secrets Leak
# https://learnsome.tech/courses/security-course/watch?lesson=m02l01
# © LearnSome.tech
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
