#Write a program for a temperature converter. Prompt the user to enter a temperature in Celsius.
#If the temperature is below freezing (0°C or lower), print a message recommending
#to wear warm clothes. If it's above 30°C, suggest staying hydrated.
temp=int(input("enter the temperature"))
if temp<=0:
        print("wear warm clothes for your safety")
if temp>0 and temp<=30:
        print("the weather is fair")
if temp>30:
        print("stay hydrated")
#NOTE:in this programme first it is asked to convert temperature but then nothing
        #like this is shown.so this first line to confuse so just focus on description.
