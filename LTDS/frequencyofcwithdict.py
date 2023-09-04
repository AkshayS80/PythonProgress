#WAP to find the frequency of characters in a string.

str1="this is a python programming lab"
all_freq={}
for i in str1:
    if i in all_freq:
        all_freq[i]+=1
    else:
        all_freq[i]=1
print("The count of all characters in the string is:\n",all_freq)