x=int(input("enter the value"))

if x<0:
    print("given number is an negative number")
elif x>0:
    print("given number is an positive number")
elif x==0:
    print("given number is equals to zero")
else:
    print("number not specified")

#to find the highest number

a=129
b=567
c=4

if a>b and a>c:
    print("highest number is a: "+str(a))
    print(f'{"highest number is : "}{a}')
elif b>c:
    print("highest number is b: "+str(b))
    print(f'{"highest number :"}{b}')
else:
    print("highest number is c: "+str(c))
    
    
y=input("enter the number")