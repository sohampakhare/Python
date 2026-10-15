#File Comparison Compare two files and print whether their contents are identical.
with open("myfile.txt","r") as f1, open("sample.txt","r") as f2: 
    if f1.read()==f2.read():
        print("identical...")
    else:
        print(" Not identical...")