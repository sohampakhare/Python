#Print Specific Line Print the 3rd line from myfile.txt using readlines().

with open("myfile.txt","w") as f2: # open and read file

    s="Welcome to the magical world of Python"
    f2.write('''hello every one 
    my name is soham pakhare
     i am from pune
     lest start the assignment''')
    

with open("myfile.txt","r") as f: # open and read file
    s=f.readlines()
    print(s[2])