a=int(input("Enter largest number: "))
b=int(input("Enter smallest number: "))
e=a
f=b
while(b):
    c=b
    b=a%b
    a=c
d=e*f
print("LCM is", d/c)
