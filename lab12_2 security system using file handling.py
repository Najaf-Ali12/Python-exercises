# LAB12_2: write a programme that implements a small-scale security surveilance system. the programme allow the user to enter name, phone number
#and then the information in the log file along with the arrival time information
import datetime
file=open("studentrecord.txt","a")
name=input("enter your name:")
phone=input("enter your phone number:")
currenttime=datetime.datetime.now()
racord=file.write(f"the visitor name is {name}, his phone number is {phone} and he came on {currenttime} \n")                                             #this is to print current time, 
#variable=datetime.datetime.now().date()    this will print current date
#variable=datetime.datetime.now()      this will print both current date and current time
