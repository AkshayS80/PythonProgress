# WAP to add two matrices 

A=[]
a=int(input("Enter the number of rows:"))
b=int(input("Enter the number of columns:"))
print("Enter the element:")
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
print("Enter the element:")
for i in range(a): 
    row=[]                                        
    for j in range(b): 
       row.append(int(input()))             
    B.append(row)                            

print("Matrix B:")
for i in range(a):
    for j in range(b):
        print(B[i][j], end=" ")
    print() 

result = [[0,0,0], [0,0,0], [0,0,0]] 
print("Adding the two matrices...")
for i in range(a):    
    for j in range(len(A[0])): 
        result[i][j] = A[i][j] + B[i][j] 
for r in range: 
    print("Resultant Matrix is:",r) 