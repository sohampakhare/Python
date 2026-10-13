
#Write a program to read a file and count how many vowels  are present in the count

with open("file1.txt","r") as f:

  s=f.read()
  count = 0

for ch in s.lower():

    if ch in ["a", "e", "i", "o","u"]:

     count+=1

print(f"Number of vowels: {count}")
