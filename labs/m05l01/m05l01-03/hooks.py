# Application Security & Threat Modeling for Engineers — lesson m05l01 — Dependency Risk And Typosquatting
# https://learnsome.tech/courses/security-course/watch?lesson=m05l01
# © LearnSome.tech
import os

def get_requires_for_build_wheel(config_settings=None):
    print("  [hook] arbitrary code, before a single file is installed")
    print("  [hook] can i read the environment:", len(os.environ) > 0)
    print("  [hook] can i write to the disk: yes, see below")
    open("stolen.txt", "w").write("written during the build\n")
    return []

def build_wheel(wheel_dir, config_settings=None, metadata_dir=None):
    return "friendly_utils-1.0.0-py3-none-any.whl"
