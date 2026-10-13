#Take a sentance from user ,Split in into words and store them in a list .print the loingest word.

sentence =input("Enter a sentence: ")

words = []
lw=""
for word in sentence.split():
    words.append(word)

if len(word)>len (lw):
    lw = word

print(f"Longest word: {lw}")