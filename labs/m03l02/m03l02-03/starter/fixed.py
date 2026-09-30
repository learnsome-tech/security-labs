import sqlite3
con=sqlite3.connect(':memory:')
con.execute('create table users (name, secret)')
rows=[('alice','a1'),('bob','b2')]
con.executemany('insert into users values (?, ?)', rows)
name="alice' OR '1'='1"
print(con.execute('select name from users where name=?',(name,)).fetchall())
