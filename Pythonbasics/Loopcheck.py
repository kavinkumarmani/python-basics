'''
Created on Aug 11, 2019

@author: Saran
'''
num=[2,3,4,5,6,7,8,9]
for i in num:
    print(i)
else:
    print("number completed")
    
name=["kavi","arun","jaya","praveen","sasi"]
for index in range(len(name)):
    print(name[index])
    
for i in range(1,5):
    for j in range(i):
        print(i,end="")
    print()