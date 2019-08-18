'''
Created on Jul 31, 2019

@author: Saran
'''
count=0

while count<3:
    print("Hello World")
    count=count+1
else:
    print("while loop over")
    
#for loop

num=[1,2,3,4,5,6,8]
for i in num:
    print(i)
    
name=["asd","ert","rtye","yutr","rete"]
for i in name:
    print(i)

name="kavinkumar"
for i in name:
    print(i)
    
List=["kavin","automation","labs"]
for index in range(len(List)):
    print(List[index])
    
List=["ashiq","dinesg","ganesh","ravi"]
for index in range(len(List)):
    print(List[index])
else:
    print("name is completed")
    
for i in range(1,5):
    for j in range(i):
        print(i,end="")
    print()
