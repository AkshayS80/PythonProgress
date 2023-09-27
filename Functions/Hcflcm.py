## WAP to form two function blocks that calculate the HCF and LCM of two numbers

def HCF():
  a=int(input("Enter the first number"))
  b=int(input("Enter the second number"))
  if a<b:
    smaller=a
  else:
    smaller=b
  for i in range(1,smaller+1):
    if(a%i==0 and b%i==0):
      hcf=i
  print("The HCF is",hcf)

def LCM():
  a=int(input("Enter the first number"))
  b=int(input("Enter the second number"))
  if a>b:
    greater=a
  else:
    greater=b
  while True:
    if (greater%a==0 and greater%b==0):
      lcm=greater
      break
    greater+=1
  print("The LCM is",lcm)

print("1.HCF\n2.LCM\n3.Exit")
choice=int(input("Enter a choice"))
while True:
  if choice==1:
    HCF()
  elif choice==2:
    LCM()
  elif choice==3:
    break
  else:
    print("Enter a valid choice")
