#WAP to print fibonacci series
n=int(input("Enter the number of terms:"))
print("Fibonacci Series")
print("0")
print("1")
a=0
b=1
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)