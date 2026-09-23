# Application Security & Threat Modeling for Engineers — lesson m02l02 — The Environment Variable Trap
# https://learnsome.tech/courses/security-course/watch?lesson=m02l02
# © LearnSome.tech
import os, subprocess, sys

os.environ["API_TOKEN"] = "sk-live-4d1f-demo"

PROBE = ("import os;"
         "print('child sees API_TOKEN:', os.environ.get('API_TOKEN'))")

narrow = {"PATH": os.environ["PATH"], "LANG": "C"}

print("the service still holds the token")
subprocess.run([sys.executable, "-c", PROBE], env=narrow)
print("the child was given an environment, not handed ours")
