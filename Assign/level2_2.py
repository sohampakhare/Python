#Append Mode Add This is appended text from write your name  to the
#end of a file without overwriting existing content.

with open("myfile.txt","a") as f: # open and read file
    f.write(" \n this ia appended text from  soham")

with open("myfile.txt",'r')as f:
    print(f.read())

