#WAP to convert from F to C and Vice versa
num=int(input("Enter the conversion type/n 1.F --> C --1 /n 2.C --> F /n"))
if num==1:
    f=int(input("Enter the Farenheit Temp"))
    c=(f-32)/1.8
    print("The celsius temp of",f,"is",c)
elif num==2:
    c=int(input("Enter the Farenheit Temp"))
    f=(c*1.8)+32
    print("The Farenheit temp of",c,"is",f)
else:
    print("Not valid")