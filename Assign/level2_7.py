#Line Numbering Print each line with its line number (like 1: First line).

with open("myfile.txt",'r') as f:
    s=f.readlines()
    for i in range(len(s)):
        print(f"line {i+1} :- { s[i]}")
