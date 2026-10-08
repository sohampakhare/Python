#reverse a string
s=input("enter a string :")
rev=""

for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
print("reverse string : ",rev)
