#lab4_1                                  #output of lab4_1
num=int(input("enter a number:"))        #enter a number:4
if num>=0:                               #4 is even
    if num%2==0 and num!=0:
        print(num,"is even")             #output of lab4_2
    elif num%2!=0:                       #enter any letter of english alphabet:y
        print(num,"is odd")              #y is a consonant letter
    else:                                                        #output of lab4_3
        print("it is zero")                                      #enter the person's age:78
else:                                                            #enter the employment status:working
    print("enter positive numbers to check")                     #enter the marital status:married
#lab4_2                                                          #insurance plane=1200PKR/MONTH
vowel=["a","e","i","o","u"]                                      
letter=input("enter any one letter of english alphabet:")
if letter in vowel:                                              #OUTPUT OF LAB4_4
    print(letter,"is a vowel letter")                            #enter the obtained marks:99
else:                                                            #GRADE-A1
    print(letter,"is a consonant letter")
#lab4_3
    person_age=int(input("enter the person's age:"))
employment_status=input("enter the employment status:")
marital_status=input("enter the marital status:")
if person_age<25:
    print(" ")
elif(employment_status=="any"):
    print(" ")
elif(marital_status=="unmarried"):
    print(" insurance plane=200PKR/MONTH")
if person_age>25 and person_age<=40:
    print(" ")
elif(employment_status=="unemployed"):
    print(" ")
elif(marital_status=="married"):
    print(" insurance plane=1200PKR/MONTH")
    if person_age>25 and person_age<=40:
        print(" ")
elif(employment_status=="employed"):
    print(" ")
elif(marital_status=="married"):
    print(" insurance plane=1000PKR/MONTH")
else:
    print("1500PKR/MONTH")
#lab4_4
obtained_marks=int(input("enter the obtained marks"))
if obtained_marks>41 and obtained_marks<=50:
    print("GRADE-D")
elif obtained_marks>50 and obtained_marks<=60:
    print("GRADE-C")
elif obtained_marks>60 and obtained_marks<=70:
    print("GRADE-B")
elif obtained_marks>70 and obtained_marks<=80:
    print("GRADE-A")
elif obtained_marks>80 and obtained_marks<=100:
    print("GRADE-A1")
