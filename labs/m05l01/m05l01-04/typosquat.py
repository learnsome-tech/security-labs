# Application Security & Threat Modeling for Engineers — lesson m05l01 — Dependency Risk And Typosquatting
# https://learnsome.tech/courses/security-course/watch?lesson=m05l01
# © LearnSome.tech
from difflib import SequenceMatcher

POPULAR = ["requests", "urllib3", "colorama", "python-dateutil"]
NEAR_KEYS = {"o": "ip", "u": "yi", "e": "wr", "3": "24"}
WANTED = ["requests", "colourama", "urllib4", "python-datutil", "reqiests"]

def one_edit(a, b):
    diff = [o for o in SequenceMatcher(None, a, b).get_opcodes()
            if o[0] != "equal"]
    if len(diff) != 1:
        return None
    _, i1, i2, j1, j2 = diff[0]
    return (a[i1:i2], b[j1:j2]) if max(i2 - i1, j2 - j1) == 1 else None

for name in WANTED:
    near = [(p, one_edit(name, p)) for p in POPULAR if one_edit(name, p)]
    if name in POPULAR:
        print("ok      ", name)
        continue
    real, (got, want) = near[0]
    slip = bool(got) and got in NEAR_KEYS.get(want, "")
    print("SUSPECT ", name, "- one edit from", real, "- key slip:", slip)
