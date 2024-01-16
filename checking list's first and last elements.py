n1=[]
t=int(input("tell the number of elements of your list"))
for i in range(1,t+1):
    x=int(input(f"what should come at position {i} in list"))
    n1.append(x)
print("your list is ",n1)
if n1[0]==n1[-1]:
    print("first and last element of your list is same")
else:
    print("first and last element of your list is not same")

