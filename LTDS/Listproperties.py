#WAP to use the list properties of traversing, concatenation, slicing and find the min and max of both list


l1=[1,2,3,4,5,6,7]
l2=[10,11,12,13,14,15,16,17]
for i in range(len(l1)):
  print(l1[i])
for j in range(-len(l2),-1,-1):
  print(l2[j])

l3=l1+l2
print(l3)

print(l1[0:4])
print(l2[-1:-5:-1])

print("Maximum of list 1",max(l1))
print("Maximum of list 2",max(l2))
print("Minimum of list 1",min(l1))
print("Minimum of list 2",min(l2))
