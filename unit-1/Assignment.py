
#create a list of 10 numbers print the sum of  last 4 element of thr list  find ou t he defrant betwwen maximum and minimum 3insert a number in a list in a 6 th position this number must be 1/3 of number stored at 4th position

#create a list print sum of last 4 element and print
my_list=[10,8,12,13,54,14,20,30,40,20]
#n=sum(my_list([-4:]))
n = sum(my_list[-4:])
print("sum ",n)



#2 finding diffrant between max min in this list
my_list=[10,8,12,13,54,14,20,30,40,20]
diff=max(my_list)-min(my_list)
print(diff)


#3insert number at 6th position is num is 1/3 num of 4th number
my_list=[10,8,12,13,54,14,20,30,40,20]
n=my_list[3]//3
my_list.insert(5,n)
print("after adding element : ",my_list)