#WAP to find all the odd numbers in a given range
ll=int(input("Enter the lower limit:"))
ul=int(input("Enter the upper limit:"))
print(f"The odd numbers in between {ll} and {ul} are")
for i in range(ll+1,ul):
    if i%2!=0:
        print(i)
