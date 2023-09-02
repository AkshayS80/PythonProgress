#WAP to find a factorial of a number using recursion

def fac(num):
    if num==1:
        return num
    else:
        return num*fac(num-1)


n=int(input("Enter a number:"))
if n<=-1:
    print("Factorials of negative numbers don't exist.")
elif n==0:
    print("The factorial of 0 is 1")
else:
    result=fac(n)
    print("The factorial of",n,"is",result)