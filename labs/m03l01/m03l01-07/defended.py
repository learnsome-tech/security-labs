# Application Security & Threat Modeling for Engineers — lesson m03l01 — Injection In All Its Forms
# https://learnsome.tech/courses/security-course/watch?lesson=m03l01
# © LearnSome.tech
import sqlite3, subprocess

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE doc (owner TEXT, body TEXT)")
db.executemany("INSERT INTO doc VALUES (?, ?)",
               [("alice", "budget"), ("bob", "lunch")])
SORTABLE = {"owner", "body"}

def find(owner, order):
    if order not in SORTABLE:
        return "rejected order column: " + order
    sql = "SELECT body FROM doc WHERE owner = ? ORDER BY " + order
    return [row[0] for row in db.execute(sql, (owner,))]

print("normal:", find("bob", "body"))
print("attack:", find("bob' OR '1'='1", "body"))
print("bad order:", find("bob", "body; DROP TABLE doc"))
done = subprocess.run(["cat", "report.txt; echo I-am-running-as-you"],
                      capture_output=True, text=True)
print("no shell:", done.stderr.strip().split(": ")[-1])
