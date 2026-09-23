# Application Security & Threat Modeling for Engineers — lesson m02l02 — The Environment Variable Trap
# https://learnsome.tech/courses/security-course/watch?lesson=m02l02
# © LearnSome.tech
import os, sys

def setting(name):
    value = os.environ.get(name)
    if value is None:
        sys.exit("missing required setting: " + name)
    return value

token = setting("API_TOKEN")
print("token loaded from the environment:", "sk-live-" + token[-4:])
print("the source file holds no credential")
print("the deployment holds it instead")
