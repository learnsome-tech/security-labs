# Application Security & Threat Modeling for Engineers — lesson m02l02 — The Environment Variable Trap
# https://learnsome.tech/courses/security-course/watch?lesson=m02l02
# © LearnSome.tech
import os, stat

FD_PATH = "token"

with open(os.open(FD_PATH, os.O_CREAT | os.O_WRONLY, 0o600), "w") as out:
    out.write("sk-live-4d1f-demo")

mode = stat.S_IMODE(os.stat(FD_PATH).st_mode)
print("mode on the secret file:", oct(mode))
print("group or other can read it:", bool(mode & 0o044))

with open(FD_PATH) as handle:
    token = handle.read()

print("token read from the file:", "sk-live-" + token[-4:])
print("token in the environment:", os.environ.get("API_TOKEN"))
