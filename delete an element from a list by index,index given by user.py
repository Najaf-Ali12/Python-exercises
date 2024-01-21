#Python program to delete an element from a list by index
#index given by user
list1=[1,2,3,4,5,"6",7,8,True,0,2,4,5,6,"cat",33]
print("original list is ",list1)
index=int(input("enter the index of element you want to delete"))
list1.pop(index)
print("updated list is ",list1)


#Python program to delete any element from a list 
#element given by user
list1=[1,2,3,4,5,"6",7,8,True,0,2,4,5,6,"cat",33]
print("original list is ",list1)
element=input("enter the element of original list that you want to remove")
list1.remove(element)
print("updated list is ",list1)
