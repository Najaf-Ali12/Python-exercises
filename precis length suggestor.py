text=input("enter the passage:")
original=list(text).remove(" ")
print(len(text))
textlength=len(text)-len(str(original))+1
print(f"your given passage contains {textlength} characters")
print(f"your precis should be of {round(textlength/3)} characters")