# Write a program that takes a list of integers as input and outputs a new list containing only the even integers using a while loop.

a=[1,2,3,4,5,6,7,8]
i=0
even=[]
while i<len(a):
    if a[i]%2==0:
        even.append(a[i])
    i=i+1
print(even)
