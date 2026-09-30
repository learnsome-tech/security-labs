import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE doc (id INTEGER, owner TEXT, body TEXT)")
db.executemany("INSERT INTO doc VALUES (?, ?, ?)",
               [(1, "alice", "budget"), (2, "bob", "lunch")])

def find(owner):
    sql = "SELECT body FROM doc WHERE owner = '" + owner + "'"
    print("sql:", sql)
    return [row[0] for row in db.execute(sql)]

print("normal:", find("bob"))
print("attack:", find("bob' OR '1'='1"))
