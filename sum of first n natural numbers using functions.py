#sum of first n natural numbers using for loop
n=int(input("enter a number"))
s=0
for i in range(1,n+1):
        s=s+i
print("sum of first",n,"natural numbers is",s)






#sum  of first n  natural numbers

def sum(n):
        if n==1:
         return 1
        return n+sum(n-1)
n=int(input("enter a number"))
x=sum(n)
print("sum of  first",n,"natural numbers is",x)


