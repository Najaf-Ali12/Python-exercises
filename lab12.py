#lab12_1
new=open("sample.txt","a")
for i in range(2):
    name=input("enter your name:")
    num=input("enter the number:")
    result=new.write(f"{i+1},{name}:{num}\n")
    print(result)
#lab12_2
import datetime
file=open("studentrecord.txt","a")
name=input("enter your name:")
phone=input("enter your phone number:")
currenttime=datetime.datetime.now()
racord=file.write(f"the visitor name is {name}, his phone number is {phone} and he came on {currenttime} \n")                                             