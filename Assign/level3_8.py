with open("myfile.txt","r") as file:
     lines = file.readlines()



with open("reverse_sample.txt", "w") as rfile: 
     rfile.writelines (lines[::-1])

with open("reverse_sample.txt","r") as rfile: 
     print(rfile.read())