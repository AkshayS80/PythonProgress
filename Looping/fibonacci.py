a=0
b=1
i=1
n=int(input("Enter the number of terms:))
print("Fibonacci series...\n)
print(a,b,end='')
while(i<=n-2):
  c=a+b
  print(c,end='')
  a=b
  b=c
  i+=1
