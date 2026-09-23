# Application Security & Threat Modeling for Engineers — lesson m01l01 — The Threat Model Habit
# https://learnsome.tech/courses/security-course/watch?lesson=m01l01
# © LearnSome.tech
PROMPTS = {
    "S": "can someone pretend to be this?",
    "T": "can someone change it in flight?",
    "R": "can someone deny doing it?",
    "I": "can someone read what they should not?",
    "D": "can someone exhaust it?",
    "E": "can someone gain rights they were not given?",
}
ENTRY = {"name": "password reset", "mitigated": "STRID"}

missing = [k for k in PROMPTS if k not in ENTRY["mitigated"]]
print("entry point:", ENTRY["name"])
for letter in PROMPTS:
    state = "answered" if letter in ENTRY["mitigated"] else "OPEN"
    print(" ", letter, state, PROMPTS[letter])
print("open questions:", len(missing))
