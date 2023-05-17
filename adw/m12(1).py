# Write a program that takes a list of integers as input and outputs the largest integer in the list using a while loop

list=[99,12,15,20,17]
i=0
j=0
# a=list[0]
# b=len(list)
# while i<b:
#     if list[i]>list[i+1]:
#         print(list[i])
#         j=j+1
#         j+=1    
#     i=i+1
numbers = [100,1,2,5,8,4,99,3]

x = 0
y = numbers[x]
while x < len(numbers):
  if numbers[x] > y:
    y = numbers[x]
  x = x+1
print (y)