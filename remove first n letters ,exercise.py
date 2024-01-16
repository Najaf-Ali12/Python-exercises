#write a programme that will remove first n
#letters from a word
#note:word and n should be taken from user
word=input("enter a word")
n=int(input("enter a number"))
print("the word obtained after removing first",n,"letters from",word,"is" ,word[n::])
