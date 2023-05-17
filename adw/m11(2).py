# Write a program that takes a string as input and outputs the string in reverse order using a while loop

str='Hello'
i=0
while i<len(str):
        i=i+1
        print(str[::-i])
        break
        