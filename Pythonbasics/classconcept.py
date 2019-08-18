'''
Created on Aug 11, 2019

@author: Saran
'''

class addition:
    a=4
    b=5
    
    def __init__(self):
        print("class constructor")
        
        
    def sum(self,a,b):
        c=a+b
        print(c)
        
    def multi(self,a,b):
        c=a*b
        print(c)
        
    def div(self,a,b):
        c=a/b
        print(c)
    
    
a1=addition()
a1.div(addition.a,addition.b)