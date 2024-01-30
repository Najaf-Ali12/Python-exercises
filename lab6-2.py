#generates the list of 20 random numbers print the list,the largest and the 
#the smallest number in list
import random
list1=[]
for i in random.sample(range(1,100),20):
    list1.append(i)
print(list1)
print("maximum number from 20 random numbers is: ",max(list1))
print("minimum number from 20 random numbers is:",min(list1))