#write a python programme that prompt the user to enter 5 numbers.
#stores them in a list and then prints the sum of all even numbers in a list.
list1=[]
sum=0
for i in range(5):
    n=int(input("enter the number"))
    list1.append(n)
    if n%2==0:
        sum+=n
print("list of given numbers is",list1)
print("sum of given even numbers is :",sum)