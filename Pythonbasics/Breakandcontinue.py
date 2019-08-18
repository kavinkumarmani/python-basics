'''
Created on Aug 11, 2019

@author: Saran
'''
name="kavinkumar"

for i in name:
    print(i)
    if(i=='n'):
        break
    
for i in name:
    print(i)
    if(i=='n'):
        continue
    
names=["arun","jaya","kavin","praveen","ftr"]

for i in range(len(names)):
    print(names[i])
    if(names[i]=="kavin"):
        continue