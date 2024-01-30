#print the list of odd numbers from 1 to 1000 and print their sum as well

listodd=[]
sum=0
for i in range(1,1001):
    if i%2==1:
        listodd.append(i)
        sum+=i
print(listodd)
print(sum)