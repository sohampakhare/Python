#piramid pattern

n=5

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,i*2):

        print("* ",end=" ")
    print()
  


#piramid pattern  but print altarnet line altarnet simbol

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    if i%2==0 :
        for k in range(1,i*2):
            print("* ",end=" ")
    else:
        for k in range(1,i*2):
                    print("+ ",end=" ")
        
       
    print()
  
        
     
     