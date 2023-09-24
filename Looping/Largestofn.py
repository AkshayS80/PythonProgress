## WAP to find the largest of n numbers.

n=int(input("Enter the number of numbers:"))
Max=int(input("Enter the first number:"))
i=1
while(i<=n):
    ele=int(input("Enter an element:"))
    if ele>Max:
        Max=ele
    i+=1

print(f"The largest number is {Max}")
