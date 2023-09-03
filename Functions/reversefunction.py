#WAP to find the reverse of a number 

def reversed(num):
    rev=0
    while num!=0:
        digit=num%10
        rev=rev*10+digit
        num//=10
    return rev  
        
n=int(input("Enter a number:"))
result=reversed(n)
print("The reversed number is",result)
