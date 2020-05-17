#The driving code
from script1 import Graph
import sqlite3
from script3 import updatetime,create,view,insert,query,updatecontact,updatecolor,querycolor
from script4 import welcome,reg
from new_user import user_create,user_view,user_query,user_insert
create()
user_create()
reg()
red=welcome()

edges=[]
user={}
color={}
rows=view()
for i in rows:
    user[i[0]]=i[3].rstrip()
    color[i[0]]=i[4]
print(user)
for j in user.keys():
    for i in (user[j].split(" ")):
        if(user[j]!=''):
            edges.append((j,int(i)))

if(red!=None):
    g=Graph(edges)
    no,orange=g.bfsq(red)
    for i in orange:
        rows=view()
        for j in rows:
            if(j!=' '):
                contacts=j[3].rstrip().split(' ')
                time=j[3].rstrip().split(' ')
                if (str(i) in contacts and time[contacts.index(str(i))]!=' ' and int(time[contacts.index(str(i))])<=14 and colorquery(i)!='R'):
                    updatecolor(i,'O')
                    color[i]='O'
    updatecolor(red,'R')
    color[red]='R'


updatetime()
