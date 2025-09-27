a=int(input("Enter largest number: "))
b=int(input("Enter smallest number: "))

while(b):
    c=b
    b=a%b
    a=c
print("HCF is",c)
