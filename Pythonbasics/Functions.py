 '''
Created on Aug 1, 2019

@author: Saran
'''
def key():
    print("hai hello")
    
key()

def value(x):
    print(x+10)
    
value(45)

#optional parameter

def checkname(name="kavin"):
    print(name)
    
checkname("arun")

name=["arun","kavin","jaya","saran"]

def frequentnames(list):
    for i in list:
        print(i)
        
frequentnames(name)

#Checking
#to find factorial of the number using recrusion function

def fact(j):
    if(j>1):
         j=j*fact(j-1)
    return j

print (fact(5))

def login(username,password):
    print("login with %s and %s"% (username,password))
    
login("kavin9965755008@gmail.com","Password@123")
