import subprocess, sys

SERVICE = """
import os
def render(template):
    raise RuntimeError("template step failed")
try:
    render("invoice")
except RuntimeError as err:
    print("internal error:", err)
    print("diagnostics, environment follows:")
    for key in sorted(os.environ):
        if not key.startswith("_"):
            print(" -", key, "=", os.environ[key])
"""

ENV = {"PATH": "/usr/bin", "LANG": "C.UTF-8", "SERVICE": "billing",
       "API_TOKEN": "sk-live-4d1f-demo"}

subprocess.run([sys.executable, "-c", SERVICE], env=ENV)
