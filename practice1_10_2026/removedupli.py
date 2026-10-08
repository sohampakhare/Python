# removing duplicate from list
s=[11,22,11,33,11,22,44,55,66,55]
r=[]

for i in s:
    if i not in s:
        r.append(i)
print(r)
    