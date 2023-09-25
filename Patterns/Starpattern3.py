# WAP to create a star pattern
# * * * * *
# * * * *
# * * * 
# * *
# *

num=int(input("Enter the number of rows:"))
for i in range(num,1,-1):
  for j in range(i,1,-1):
    print("*")
  print("\n")
