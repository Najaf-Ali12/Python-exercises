#Create a function that checks if a given word is a palindrome.
#Test the function with words like "level" and "python.“
#palindrome means anything which doesnot change when it is reversed
def check():
        t=word[::-1]
        #if we have list we will use reverse method for reverse
        #if we have not list we will use [::-1] for reverse
        if t ==word:
                print("yes,",word,"is palindrome")
        else:
                print("no,",word,"is not palindrome")
word=input("enter any word")
check()
