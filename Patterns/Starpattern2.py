#WAP to print the following pattern
# H
# H E
# H E L
# H E L L
# H E L L O

word="HELLO"
rows=5
for i in range(rows):
    for j in range(i+1):
        print("word[j]",end="")
    print("\n")