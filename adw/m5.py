a=['apple','mango','cherry','grape']
b=len(a)
i=0
d={}
# length=[]
while i<b:
    d[a[i]]=len(a[i])
    # length.append(len(a[i]))
    i=i+1
    dk=d.values()
print(dk)


