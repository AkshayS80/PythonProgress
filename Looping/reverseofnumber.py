#WAP to find the reverse of a number 

n=int(input("Enter a number:"))
rev=0

while n!=0:
    digit=n%10
    rev=rev*10+digit
    n//=10

print("The reversed number is",rev)