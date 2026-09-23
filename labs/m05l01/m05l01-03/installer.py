# Application Security & Threat Modeling for Engineers — lesson m05l01 — Dependency Risk And Typosquatting
# https://learnsome.tech/courses/security-course/watch?lesson=m05l01
# © LearnSome.tech
import importlib, os, sys, tomllib

table = tomllib.load(open("pyproject.toml", "rb"))["build-system"]
sys.path[:0] = table.get("backend-path", [])
print("installer: the package declares a build backend")
backend = importlib.import_module(table["build-backend"])
print("installer: asking the backend what it needs")
backend.get_requires_for_build_wheel(None)
print("installer: asking the backend to build")
print("installer: got", backend.build_wheel("dist"))
print("left behind by the build:", os.path.exists("stolen.txt"))
