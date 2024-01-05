#write a programme that prints the table of number entered by the user
#using both for and while loop

#1:using for loop
n=int(input("enter a number"))
for i in range(1,11):
   print(i,"x",n,"=",i*n)
print("table  of ",n,"has been created for you")
i=1



#2:using while loop
n=int(input("enter the number"))
while i<=10:
   print(i,"x",n,"=",i*n)
   i+=1
print("table of",n,"is ready for you")



