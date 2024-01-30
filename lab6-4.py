#create the tuple containing the name of  5 countries.Write a programme that
#iterates through the tuple and print only the countries length greater than 7
country=("pakistan","india","oman","somalia","bangladesh")
for i in country:
    if len(i)>6:
        print(i)