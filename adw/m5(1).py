txt='Hello'
a=len(txt)
# print(a)
i=0
j=0
k={}
t=''
count=0
while i<a:
         if txt[i] not in t:
                count=1
                t+=txt[i]
                k[txt[i]]=count
         else:      
              count+=1
              t+=txt[i]
         k[txt[i]]=count
        #  j=j+1

         i=i+1
# print(t)
print(k)