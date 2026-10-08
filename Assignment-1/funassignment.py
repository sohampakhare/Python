#
name="soham"
v="aeiou"
for i in v:
    name=name.replace(i,"z")
print(name)

#create list of numbes and string accept value from user and seprate the list from the maximum number display the names in a desending order
ml=[]
n=int(input("enter number of iteams"))
for i in range(n):
    e=input("enter value")
    if e.isdigit():
        ml.append(int(e))
    else:
        ml.append(e)
print(ml)
