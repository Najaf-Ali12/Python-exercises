#lab5_1
for numbers in range(100,151):
    print(numbers)
#lab5_2
for evens in range(50,101,2):
    print(evens)
#lab5_3
for odds in range(101,150,2):
    print(odds)
#lab5_4
#using for loop
num=int(input("enter the number whose tabel you want to generate:"))
print("the required table of",num,"is given below")
for table in range(num,num*11,num):
    for multiplier in range(1,11):
        print(multiplier,"x",num,"=",table)

