#
with open('file1.txt', 'r') as f :
    arr=f.readlines()

    print("total num of lines : ",len(arr))
    print(arr[1])
    print(arr[3])