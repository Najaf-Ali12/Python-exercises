#make a python programe that will find the maximum number.from how many numbers to find,decission should depend on the user.
max=0
list1=[]
while True:
    try:
        num=float(input("enter a number:"))
        list1.append(num)
        if num>max:
            max=num
        choice=input("do you want to add another number(enter yes or no):")
        if choice.lower()=="no":
            break
    except:
        print("you should enter a numbers")
print("the list of numbers you entered is",list1)
print("the maximum number is",max)