#to find whether the number is a perfect square or not
num=int(input("enter a number"))
for i in range(1,num//2+1):
    if i**2==num:
        print(num,"is a perfect square")
        break
    if i==num//2:
        print(num,"is not a perfect square")
        break