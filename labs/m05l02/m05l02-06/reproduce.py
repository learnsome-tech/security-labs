# Application Security & Threat Modeling for Engineers — lesson m05l02 — Lockfiles And Reproducible Builds
# https://learnsome.tech/courses/security-course/watch?lesson=m05l02
# © LearnSome.tech
import hashlib, io, zipfile

SOURCE = b"def main():\n    return 'the same source, every time'\n"
def build(stamp):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        entry = zipfile.ZipInfo("app/main.py", date_time=stamp)
        archive.writestr(entry, SOURCE)
    return hashlib.sha256(buffer.getvalue()).hexdigest()[:24]

monday = (2026, 3, 2, 9, 15, 0)
tuesday = (2026, 3, 3, 17, 40, 0)
pinned = (1980, 1, 1, 0, 0, 0)
print("built on monday: ", build(monday))
print("built on tuesday:", build(tuesday))
print("byte identical:", build(monday) == build(tuesday))
print("with the clock pinned:", build(pinned))
print("and pinned again:     ", build(pinned))
print("byte identical:", build(pinned) == build(pinned))
