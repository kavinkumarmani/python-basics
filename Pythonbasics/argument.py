'''
Created on Aug 11, 2019

@author: Saran
'''
def login(username,password):
    print(username,password)
login(username="kavin", password="test1234")

#^arg

def sum(*arg):
    for i in arg:
        print(i)
sum(2,3,4,5,6,7,8)

def sum1(**args):
    for key,value in args.items():
        print("%s==%s"%(key,value))
sum1(apple=50,orange=60)

def getmarks(**args):
    for key,value in args.items():
        print("%s==%s"%(key,value))
getmarks(kavin=45,arun=60,jayanth=90)


cube=lambda x: x*x*x
print(cube(5))
value=lambda y:y*5
print(value(8))
square=lambda z:z*z
print(square(9))
