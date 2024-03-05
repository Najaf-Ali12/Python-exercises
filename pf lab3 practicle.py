#lab3_1                                    output of lab3_1
A=int(input("enter a number:"))          #enter a number:4
B=int(input("enter a number:"))          #enter a number:5
print("addition is:",A+B)                #addition is:9
print("subtraction is:",A-B)             #subtraction is:-1
print("multiplication is:",A*B)          #multiplication is: 20
print("divison is:",A/B)                 #divison is:0.8
print("A**B:",A**B)                      #A**B:1024
print("A//B:",A//B)                      #A//B:0
print("A%B:",A%B)                        #A%B:4
#addition,multiplication and equality are commutative
#lab3_2                                  #OUTPUT OF LAB 3_2
a=int(input("enter a number:"))          #enter a number:8
b=int(input("enter a number:"))          #enter a number:6
c=int(input("enter a number:"))          #enter a number:4
print("a+(b+c):",a+b+c)                  #a+(b+c): 18
print("a-(b-c):",a-(b-c))                #a-(b-c): 6
print("a.(b.c):",a*b*c)                  #a.(b.c): 192
print("a/(b/c):",a/b/c)                  #a/(b/c): 0.3333333333333333
#multiplication and addition verify associative properity
#lab3_3                                  #OUTPUT OF LAB3_3 
a=int(input("enter a number:"))          #enter a number:8
b=int(input("enter a number:"))          #enter a number:8
print("a==b is",a==b)                    #a==b is True
print("a>=bis",a>=b)                     #a>=b is True
print("a<=b is",a<=b)                    #a<=b is True
print("a>b is",a>b)                      #a>b is False
print("a<b is",a<b)                      #a<b is False
#lab3_4                                  #OUTPUT OF LAB3_4
a=int(input("enter a number:"))          #enter a number:30
b=int(input("enter a number:"))          #enter a number:9
if a>0:                                  #both positive
    if b>0:                              #atleast one is odd
        print("both positive")           #both are multiple of 3
    else:
        print("atleast one of them is negative")
if b<0:
    if a<0:
        print("both negative")
    else:
        print("atleast one of them is positive")
if a%2==0:
    if b%2==0:
        print("both even")
    else:
        print("atleast one is odd")
if a%2!=0:
    if b%2!=0:
        print("both are odd")
    else:
        print("atleast one is even")
if a%3==0 and b%3==0:
    print("both are multiple of 3")
else:
    print("both are not multiple of 3")




