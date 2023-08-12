#WAP to print all armstrong numbers between 100 and 999
print("All of the armstrong numbers between 100 and 999 are:")
for i in range(100,1000):
    a=i
    sum=0
    while(i>0):
        rem=i%10
        sum=sum+(rem*rem*rem)
        i=i//10
    if sum==a:
        print(a)