#WAP to find the student with the highest marks and print it
# Given respectively,
# Students --> [A,B,C,D,E]
# Student Marks --> [25,26,38,44,29]
Sm=[25,26,38,44,29]
Sn=["A","B","C","D","E"]
m=len(Sm)
Max=Sm[0]
for i in range(m):
    if Max<Sm[i]:
        Max=Sm[i]
        ind=i
    else:
        continue
print(f"The student with the highest marks is {Sn[ind]} with {Sm[ind]}")