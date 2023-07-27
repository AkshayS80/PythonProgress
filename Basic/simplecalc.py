#WAP to make a simple calculator with all operations

#functions 
def add(a,b):
    c=a+b
    return c
def subtract(a,b):
    c=a-b
    return c
def multiply(a,b):
    c=a*b
    return c
def divide(a,b):
    c=a/b
    return c
def power(a,b):
    c=a**b
    return c

#main Block
print("1-Add")
print("2-Subtract")
print("3-Multiply")
print("4-Divide")
print("5-Power")
n=input("Enter the number to perform operation:-")
x=int(input("Enter number:"))
y=int(input("Enter number:"))
if n=="1":
    print("The sum is",add(x,y))
elif n=="2":
    print("The sum is",subtract(x,y))
elif n=="3":
    print("The sum is",multiply(x,y))
elif n=="4":
    print("The sum is",divide(x,y))
elif n=="5":
    print("The sum is",power(x,y))
else:
    print("Not a valid option")

