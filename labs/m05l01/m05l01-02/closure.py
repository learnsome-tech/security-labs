# Application Security & Threat Modeling for Engineers — lesson m05l01 — Dependency Risk And Typosquatting
# https://learnsome.tech/courses/security-course/watch?lesson=m05l01
# © LearnSome.tech
import json
from collections import deque

graph = json.load(open("deps.json"))
seen = {"report-cli"}
owners = set()
deepest = 0
queue = deque([("report-cli", 0)])
while queue:
    name, level = queue.popleft()
    node = graph[name]
    deepest = max(deepest, level)
    owners.update(node["maintainers"])
    for child in node["deps"]:
        if child not in seen:
            seen.add(child)
            queue.append((child, level + 1))
print("you typed one install command for: report-cli")
print("packages actually installed:", len(seen))
print("deepest transitive level:", deepest)
print("accounts that can ship you code:", len(owners))
print("any one of those accounts is enough")
