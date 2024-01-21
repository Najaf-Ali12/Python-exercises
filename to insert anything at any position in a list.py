#Python program to insert anything at any position in a list
list1=[1,2,3,4,5,"6",7,8,True,0,2,4,5,6,"cat",33]
print("original list is ",list1)
num=input("enter anything that you want to add in list")
position=int(input(f"enter the position of {num}"))
list1.insert(position,num)
print("new updated list is ",list1)
