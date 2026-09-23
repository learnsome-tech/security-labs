# Application Security & Threat Modeling for Engineers — lesson m05l03 — Software Bill Of Materials
# https://learnsome.tech/courses/security-course/watch?lesson=m05l03
# © LearnSome.tech
import json

app = json.load(open("sbom.json"))["components"]
base = json.load(open("base-image.json"))
names = {part["name"] for part in app}
print("the source build knows about:", len(app), "components")
print("the base image", base["image"], "adds:", len(base["packages"]))
for pkg in base["packages"]:
    purl = "pkg:apk/alpine/" + pkg["name"] + "@" + pkg["version"]
    print(" ", purl, "in the lockfile:", pkg["name"] in names)
print("what ships is the union:", len(app) + len(base["packages"]))
