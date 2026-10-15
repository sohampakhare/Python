#Word Frequency Counter Count how many times each word appears in a file and
#display results as a dictionary.

with open("myfile.txt","r") as file: 
    words = file.read().split()

count = {}
for word in words:
 word =word.lower()
if word in count:
  count [word] += 1
else:
 count [word]=1

print(count)