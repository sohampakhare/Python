with open("sample.txt","w") as f2: # open and read file

    s="Welcome to the magical world of Python"
    f2.write(s)
    

with open("sample.txt","r") as f: # open and read file
    s=f.read()
    print(s)