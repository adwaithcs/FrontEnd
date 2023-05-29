str='hello'
v=['a','e','i','o','u']
i=0
while i<len(str):
    if str[i] in v:
        print(str[i])
    i=i+1