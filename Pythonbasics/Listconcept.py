'''
Created on Aug 1, 2019

@author: Saran
'''
num=[1,3,5,6,7,8,9,2]
print(num[0])
print(num[6])
print(num[-5])

print(num[:])#new copy or shallow copy

print(num+[11,12,13])
print(num+["a","b","c"])

num.append("d")
print(num)

num[3]=56
print(num)

num.append(7**3)
print(num)

name=["a","b","c","d","e","g","h"]
name[2:5]=[]
print(name)

a=[1,2,3,4,5]
b=["a","b","c","d","e"]
c=[a,b]
print(c)
print(c[0][2])