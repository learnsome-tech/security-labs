# Application Security & Threat Modeling for Engineers — lesson m05l01 — Dependency Risk And Typosquatting
# https://learnsome.tech/courses/security-course/watch?lesson=m05l01
# © LearnSome.tech
import re

REVIEWED = {"requests": "2.32.3", "urllib3": "2.2.3", "colorama": "0.4.6"}
PIN = re.compile(r"^([a-z0-9][a-z0-9._-]*)==([0-9]\S*)$")
REQUESTED = ["requests==2.32.3", "urllib3>=2.0", "colorama==0.4.6",
             "leftpad-py==0.0.1"]

for line in REQUESTED:
    found = PIN.match(line)
    if not found:
        print("REJECT", line, "- not pinned to a single version")
        continue
    name, version = found.groups()
    if name not in REVIEWED:
        print("REJECT", line, "- unreviewed name, open a review")
    elif REVIEWED[name] != version:
        print("REJECT", line, "- reviewed version is", REVIEWED[name])
    else:
        print("allow ", line)
