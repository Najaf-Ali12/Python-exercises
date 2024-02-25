def gcd(num1,num2):
    smallest=num1 if num1<num2 else num2
    for i in range(1,smallest+1):
        if num1%i==0 and num2%i==0:
            g=i
    return g
def lcm(num1,num2):
    greatest=num1 if num1>num2 else num2
    while True:
        if greatest%num1==0 and greatest%num2==0:
            l=greatest
            return greatest
        greatest+=1
n1=int(input("enter first number:"))
n2=int(input("enter the second number"))
choice=input("enter either lcm or gcd as your choice:")
if choice.lower()=="lcm":
    print("the lcm is",lcm(n1,n2))
elif choice.lower()=="gcd":
    print("the gcd is",gcd(n1,n2))
else:
    print("INVALID CHOICE")



