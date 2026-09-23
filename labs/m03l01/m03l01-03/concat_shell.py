# Application Security & Threat Modeling for Engineers — lesson m03l01 — Injection In All Its Forms
# https://learnsome.tech/courses/security-course/watch?lesson=m03l01
# © LearnSome.tech
import subprocess

with open("report.txt", "w") as f:
    f.write("quarterly numbers\n")

def show(name):
    cmd = "cat " + name
    print("shell:", cmd)
    done = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return done.stdout.strip().replace("\n", " and then ")

print("normal:", show("report.txt"))
print("attack:", show("report.txt; echo I-am-running-as-you"))
