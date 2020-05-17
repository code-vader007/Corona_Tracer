#The user experience
from script1 import Graph
import sqlite3
from script3 import querycon,create,view,insert,query,updatecontact,updatecolor,querycolor
from new_user import user_query,user_insert,user_query
from getpass import getpass
import random
def reg():
    print('Welcome to the covid 19 tracker')
    print('Would you like to signup for the app?(y or n)')
    ans=input()
    if(ans=='y'):
        print('Please type your full name')
        name=input()
        print('Please type your phone number')
        number=input()
        print('Please type your condition code in capital')
        code=input()
        s=0
        while(s!=1):
            print('Please input a password')
            pwsd=getpass()
            print('Please retype your password')
            pwsd1=getpass()
            if(pwsd==pwsd1):
                s=1
            else:
                print('The passwords donot match. Please retype')

        print('You will now be given an integer id which you will use to login.Please keep it safe')
        k=random.randint(1,10000000)
        slot=query(k)
        while(slot==1):
            k=random.randint(1,10000000)
            slot=query(k)
        print('Your id is %d'%k)
        user_insert(k,name,pwsd)
        insert(k,name,number,'',code,'')
        print('Congrajulations, you are registered here.')

def welcome():
    print('Would you like to login to the app?(y or n)')
    log=input()
    if(log=='n'):
        quit()
    print('Please enter your id(which is a number) to login\n')
    ans=int(input())
    pwsd=getpass("Please enter the password:")
    tr=3
    while(tr>0):
        att=user_query(ans,pwsd)
        if(att==1):
            break
        elif(att==0):
            quit()
        else:
            print('Please retype password')
            pwsd=getpass()
        tr=tr-1
    if(tr==0):
        print('Your password donot match.Please try again later')
        quit()

    if(att!=None):
        color=querycolor(ans)
        print('Do you want to add an user(y or n)')
        ans3=input()
        if(ans3=='y'):
            if(color=='O' or color=='R'):
                print('You are not allowed to make any new contact as stated in our warning.Since you have broken the rules the officials are on your way to get you')
                quit()
            while(ans3!='n'):
                print('Give  the id of the contact you want to add')
                contact=int(input())
                if(querycon(contact)!=[]):
                    updatecontact(ans,contact)
                    print('Do you want to add another user?')

                else:
                    print("Sorry this user is not registered here.You cannot add the person")
                    quit()
                ans3=input()
    print('Do you want to change your condition color(in case you tested postive)')
    ans4=input()
    if(ans4=='y'):
        return ans
    else:
        return None
