# Write a program that takes a list of strings as input and outputs a new list containing the same strings, but with the first letter capitalized using a while loop.

a=['january','february','march','april','may']
i=0
x=[]
while i<len(a):
    x.append(a[i].capitalize())
    i=i+1
print(x)