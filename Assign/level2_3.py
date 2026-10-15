# Q6 Seek Practice Jump to the 10th character using seek() and print the next 5characters.

with open("myfile.txt",'r') as f:
    f.seek(10)
    print(f.read(5))
