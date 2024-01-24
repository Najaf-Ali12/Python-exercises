#print union of two sets
n=int(input("enter the number of elements in your set"))
set1=[]
set2=[]
for i in range(n):
    x=input("enter the element of set1:")
    y=input("enter the element of set2:")
    set1.append(x)
    set2.append(y)
set1=set(set1)
set2=set(set2)


set3 = set1.union(set2)
print(set3)

   
    #zip function
