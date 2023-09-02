#WAP to calculate the area of triangle,square and rectangle

def areaof(choice):
    if choice==1:
        h=int(input("Enter the height:"))
        b=int(input("Enter the base:"))
        return h*b
    elif choice==2:
        side=int(input("Enter the side:"))
        return side**2
    elif choice==3:
        length=int(input("Enter the length:"))
        breadth=int(input("Enter the breadth:"))
        return length*breadth
    else:
        return 'i'

print("1.Triangle")
print("2.Square")
print("3.Rectangle")
n=int(input("Enter the choice:"))
result=areaof(n)
if result=='i':
    print("Invalid choice")
else:
    print("The area is",result)