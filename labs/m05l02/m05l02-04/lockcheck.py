# Application Security & Threat Modeling for Engineers — lesson m05l02 — Lockfiles And Reproducible Builds
# https://learnsome.tech/courses/security-course/watch?lesson=m05l02
# © LearnSome.tech
import hashlib
import json
import os

for entry in json.load(open("lock.json")):
    path = os.path.join("dist", entry["file"])
    if not os.path.exists(path):
        print("FAIL ", entry["file"], "- locked, but nothing arrived")
        continue
    with open(path, "rb") as handle:
        digest = hashlib.sha256(handle.read()).hexdigest()
    if digest == entry["sha256"]:
        print("PASS ", entry["name"], entry["version"])
    else:
        print("FAIL ", entry["name"], entry["version"], "- wrong bytes")
        print("   locked", entry["sha256"][:28])
        print("   served", digest[:28])
