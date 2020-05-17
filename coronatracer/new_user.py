from script1 import Graph
import sqlite3
import random
def user_create():
    conn=sqlite3.connect('user_register.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user_register(id int,name varchar(32), password varchar(32))")
    conn.commit()
    cur.close()

def user_insert(id,name,password):
    conn=sqlite3.connect('user_register.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO user_register VALUES(?,?,?)",(id,name,password,))
    conn.commit()
    cur.close()

def user_view():
    conn=sqlite3.connect('user_register.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM user_register ")
    rows=cur.fetchall()
    conn.close()
    return rows

def user_query(id,password):
    conn=sqlite3.connect('user_register.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM user_register WHERE id = ?",(int(id),))
    data=cur.fetchall()
    if(data==[]):
        print("There is no user with this id.Please check your id and try again")
        return 0
    else:
        pwsd=data[0][2]
        if pwsd==password:
            print("Login Successful")
            return 1
        else:
            print("The password is wrong. Please try again")
            return None
    conn.commit()
    cur.close()
user_create()
user_insert(1234,"Kowshik","Windows2017")
