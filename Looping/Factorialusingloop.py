#WAP to find the factorial of a number using loop

n=int(input("Enter the number:"))
f=1
for i in range(1,n+1):
  f=f*i
print(f"the factorial of {n} is {f}")
