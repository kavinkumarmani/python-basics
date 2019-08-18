'''
Created on Aug 16, 2019

@author: Saran
'''
class name():
    
    def __init__(self,name):
        self.name=name
        
    def getname(self):
        return self.name
    
    def getsex(self):
        return "male"
    
    def employeed(self):
        return True
    
class pdetails(name):
    
    def details(self):
        return "details"
    
    def qualification(self):
        return "educated"
    
    def employeed(self):
        return False
    
N=name("kavin")
print(N.getname())
print(N.getsex())
print(N.employeed())

P=pdetails("jaya")
print(P.details())
print(P.qualification())
print(P.getname())
print(P.getsex())
print(P.employeed())

print(issubclass(pdetails,name))
print(issubclass(name,pdetails))
print(isinstance(P,pdetails))
print(isinstance(P,name ))

