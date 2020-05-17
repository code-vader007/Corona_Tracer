#The database file

import sqlite3
def view():
    conn=sqlite3.connect('db.sqlite3')
    cur=conn.cursor()
    cur.execute("SELECT * FROM user ")
    rows=cur.fetchall()
    conn.close()
    return rows

print(view())
