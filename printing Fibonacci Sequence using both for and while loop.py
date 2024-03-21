#Fibonacci Sequence:
#Generate the Fibonacci sequence up to a certain number of terms
num=int(input("enter how many numbers you want in your fibonacci sequence"))
list1=[0,1]
for i in range(num-2):
    list1.append(list1[i]+list1[i+1])
print(list1)
#finding fibonacci sequence using while loop
fibonacci_sequence=[0,1]
number=int(input("enter how many elements you want in your sequence:"))
k=0
while k<number-2:      #num-1 is because to get the same number of elements in sequence as user said
    element=fibonacci_sequence[k]+fibonacci_sequence[k+1]
    fibonacci_sequence.append(element)
    k+=1
print("required fibonaccy sequence is:",fibonacci_sequence)
#The Fibonacci sequence is a series of numbers where each number (known as a Fibonacci number) 
#is the sum of the two preceding ones, usually starting with 0 and 1. 