s1={1,2,3,4,5,6,7}
print(s1)
s2={3,4,5,2,1,4}
print(s2)
s3={2,4,6,9,7,4,4,5,5}
print(s3)

s4=set([2,3,4,5,6,6,7])
print(s4)
s5=set("phython")
print(s5)
s6=set((2,4,5,67,3,3))
print(s6)
print(max(s6))

print(4 in s4)

#arithemetic operations

#union
k1={1,2,3,4,5}
k2={4,5,6,7,8}
print(k1|k2)
print(k1.union(k2))
print(k2.union(k1))

#intersection
k3={1,3,2,4,5,6}
k4={4,5,6,7,8,9}
print(k3&k4)
print(k3.intersection(k4))
print(k4.intersection(k3))

#difference
k5={1,2,3,4,5,6}
k6={4,5,6,7,8,9}
print(k5-k6)
print(k5.difference(k6))
print(k6.difference(k5))

#symmentric difference
k7={1,2,3,4,5,6,7}
k8={4,5,6,7,8,9}
print(k7^k8)
print(k7.symmetric_difference(k8))
print(k8.symmetric_difference(k7))

#set functions
m1={1,2,3,4,5}
m1.add(6)
print(m1)

m2={1,2,3,4,5,6}
m2.update((7,8,9))
print(m2)

m3={1,2,3,4,5,67,7}
m3.clear()
print(m3)

m4={"kavin","jaya","arun"}
m5=m4.copy()
print(m5)

m6={1,2,3,4,55,6,7,8}
m6.discard(55)
print(m6)

m7={1,2,3,4,5,6,7,8}
m7.remove(7)
print(m7)