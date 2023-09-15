#WAP to find all the armstrong numbers in a given range
ll=int(input("Enter the lower limit:"))
ul=int(input("Enter the upper limit:"))

print(f"The armstrong numbers in between {ll} and {ul} are")
for i in range(ll,ul):
    num=i
    arm=0
    while i!=0:
        d=i%10
        arm=arm+d**3
        i=i//10
        if (arm==num):
            print(arm)
