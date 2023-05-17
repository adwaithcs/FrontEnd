# Write a program that takes a list of strings as input and outputs a new list containing only the strings with more than five characters using a while loop.

a=['january','february','march','april','june']
i=0
while i<len(a):
    if len(a[i])<5:
        a.remove(a[i])
    i=i+1   
print(a)