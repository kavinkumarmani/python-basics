'''
Created on Aug 11, 2019

@author: Saran
'''
def sun():
    print("sunshine")
sun()

def sum(a):
    print(a+10)
sum(10)

def getname(name="kavin"):
    print(name)
getname()

def sum1(a,b):
    c=a+b
    return c
s1=sum1(3,4)
print(s1)

def fact(num):
    if(num>1):
        num=num*fact(num-1)
    return num
print(fact(5))

def login(username,password):
    print("login with %s and %s "%(username,password))
login("kavin","password")