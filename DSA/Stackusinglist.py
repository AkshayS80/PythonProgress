# WAP to implement stack using list 

#Functions 
def isEmpty():
    if stack==[]:
        return True 
    else:
        return False
    
def Push():
    if top>MAX+1:
        print("Stack is full.")
    else:
        x=int(input("Enter an element:"))
        stack.append(x)
        print("Inserted=",x)

def Pop():
    if isEmpty():
        print("Stack is empty")
    else:
        y=stack.pop(top)
        print("Deleted=",y)

def Display():
    if stack==[]:
        print("Empty Stack")
    else:
        print("The element in the stack are:")
        for i in range(len(stack)):
            if i==len(stack)-1:
                print(stack[i],"--> Top")
            else:
                print(stack[i])
#__ main __
stack=[]
MAX=10
top=-1
choice=0
while(choice!=4):
    print("\n1.Push\n2.Pop\n3.Display\n4.Exit")
    choice=int(input("Enter a number:"))
    if choice==1:
        Push()
        continue
    if choice==1:
        Pop()
        continue
    if choice==1:
        Display()
        continue
    if choice==4:
        break
    else:
        print("Enter a valid option")
        continue