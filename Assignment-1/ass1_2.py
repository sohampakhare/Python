#read all lines from a file into a list . 
#print the total numbers of lines and display the 2nd and 4 th line


with open('file1.txt', 'r') as f :
    arr=f.readlines()

    print("total num of lines : ",len(arr))
    print(arr[1])
    print(arr[3])