# Write a program that takes two lists of integers as input and returns a list containing the common elements using a while loop

list1=[1,2,3,4,5,8]
list2=[1,2,4,6,8]
common=[]
i=0
j=0
while i<len(list1) or j<len(list2):
    if list1[i] in list2:
        common.append(list1[i])
    i=i+1
    j=j+1
print(common)

