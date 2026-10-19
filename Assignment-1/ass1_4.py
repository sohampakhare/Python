#4 th question

with open('file1.txt','r') as f:
    w=[]
    w=f.read().split()

    print("lent of words : ",len(w))

    for i in w:
        if w.count(i)==1:
            print(w,end=' ')