def gcd(a,b):
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd
def lcm(a,b):
    greatest=a if a>b else b
    while True:
        if greatest%a==0 and greatest%b==0:
            l=greatest
            return greatest
        greatest+=1
n1=int(input("enter  the first number"))
n2=int(input("enter  the second number"))
choice=input("enter what you want to do(gcd or lcm)")
if choice.upper()=="LCM":
    print("the lcm is",lcm(n1,n2))
elif choice.lower()=="gcd":
    print("the gcd is",gcd(n1,n2))
else:
    print("INVALID CHOICE")
