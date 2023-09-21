# WAP to multiply two matrices 


a=int(input("Enter the number of rows for matrix A:"))
b=int(input("Enter the number of columns for matrix A:"))
c=int(input("Enter the number of rows for matrix B:"))
d=int(input("Enter the number of columns for matrix B:"))
if b==c:
    A=[]
    print("Enter the element for matrix A:")
    for i in range(a): 
        row=[]                                        
        for j in range(b): 
            row.append(int(input()))                
        A.append(row)                               
    
    print("Matrix A:")
    for i in range(a):
        for j in range(b):
            print(A[i][j], end=" ")                  
        print() 

    B=[]

    print("Enter the element for matrix B:")
    for i in range(c): 
        row=[]                                        
        for j in range(d): 
            row.append(int(input()))             
        B.append(row)                            

    print("Matrix B:")
    for i in range(c):
        for j in range(d):
            print(B[i][j], end=" ")
        print() 
    
    result=[]
    for i in range(a):
        row=[]
        for j in range(d):
            row.append(0)
        result.append(row)
    
    print("Multiplying the two matrices...")
    for i in range(a):
        for j in range(d):
            for k in range(c):
                result[i][j] += A[i][k] * B[k][j]
                
    print("Resultant Matrix is:") 
    for i in range(a):
            for j in range(d):
                print(result[i][j], end=" ")
            print() 
else:
    print("The row of Matrix A and Matrix B are not equal.")
    print("Multiplication will not happen.")