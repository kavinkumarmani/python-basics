'''
Created on Aug 16, 2019

@author: Saran
'''
class base1():
    
    def __init__(self):
        self.str="kavin"
        print ("base1")
        
class base2():
    
    def __init__(self):
        self.str1="jaya"
        print ("base2")
        
class child(base1,base2):
    
    def __init__(self,name):
        base1.str=name
        base2.__init__(self)
        print("child")
        
    def printnames(self):
        print(self.str1,self.str)
        
ch=child("arun")
ch.printnames()
