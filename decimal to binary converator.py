num=int(input("enter a number"))
given_number=num #this is for doing string catenation in last line
binarydigits_store=[] #will store remainder
while num//2 >=1:
    remainder_store=num%2  #will takes remainder
    binarydigits_store.append(remainder_store)
    num=num//2
binarydigits_store.append(1)
binarydigits_store.reverse()
binarynumbers=''.join(map(str,binarydigits_store)) #will change list in string join all elements and store them in binarynumbers
print("the binary number for",given_number,"is",binarynumbers)
    
    
