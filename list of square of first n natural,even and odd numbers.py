#Write a Python program that generates a list of squares for numbers 1 to 10.
#Create a function to filter out odd squares and return a new list with only
#even squares.and also list having odd squares.

generallist=[]
evenlist=[]
oddlist=[]
def even_squares():
        for i in range(1,num+1):
                i*=i
                generallist.append(i)
                if i%2==0:
                  evenlist.append(i)
                elif i%2==1:
                  oddlist.append(i)
                   
        print("list of square of first",num,"natural numbers is",generallist)
        print("list of square of first",int(num/2),"even numbers is",evenlist)
        print("list of square of first",int(num/2),"odd numbers is",oddlist)
num=int(input("enter the number"))
even_squares()

        
