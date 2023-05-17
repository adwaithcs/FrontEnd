#Write a program that takes a string as input and outputs the number of words in the string using a while loop

str='Strings in python are surrounded by either single quotation marks or double quotation marks.'
i=0
a=0
words=0

while i<len(str):
    a=str.rsplit(' ')
    i=i+1
    words=len(a)
print('NowOfWords=',words)




        