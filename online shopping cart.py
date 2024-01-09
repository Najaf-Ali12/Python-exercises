#develop for an online shopping cart,Prompt the user to enter the quantity and
#price of n items.Calculate and Print the total cost.Apply a 5% discount if
#the total cost is between 100 and 200$, and a 10% discount if the total cost is
#greater than 200$
n=int(input("enter the total number of items"))
#loop will run the times items are
for i in range(n):
       quantity=int(input("enter the quantity of item"))
       price=int(input("enter the price of item, in DOLLARS "))
       total_cost=quantity*price
print("total cost is ",total_cost)
if total_cost>10 and total_cost<200:
        discount=total_cost*0.05
        bill=total_cost-discount
        print("BUT,the bill u have to pay is",bill)
elif total_cost>200:
        discount=total_cost*0.1
        bill=total_cost-discount
        print(bill)
            
