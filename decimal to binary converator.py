num=int(input("enter a number"))
x=[]
while num//2 >=1:
    y=num%2
    x.append(y)
    num=num//2
x.append(1)
x.reverse()
print(x)
    
    
