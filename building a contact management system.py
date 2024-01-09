#You are building a contact management system. Write a Python script that allows
#the user to add names to a list. After adding n  names, print the
#list and check if a specific name is in the list.
list1=[]
n=int(input("enter the number of names you want to add in list"))
for i in range(n):
        name=input("enter the name")
        list1.append(name)
print(list1)
def check():
        search=input("enter the name you want to search in list")
        if search in list1:
                print(search)
        else:
                print(search,"is not in list")
check()
