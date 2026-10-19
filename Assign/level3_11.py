#Copy Selected Lines Copy only even-numbered lines from one file into another.

with open("myfile.txt","r") as f1:
    s=f1.readlines()
with open("even.txt","a") as f:
    for i in range(0,len(s),2):
     f.write(s[i])
with open("even.txt","r") as f:
   print(f.read())
