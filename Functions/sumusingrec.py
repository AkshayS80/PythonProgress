## WAP to find the sum of n natural number using recursion

def summ(n):
    if (n!=0):
        return n+summ(n-1)
    else:
        return 0
        
num=int(input("Enter the number of natural numbers:"))
result=summ(num)
print(f"The sum of {num} numbers is {result}")
