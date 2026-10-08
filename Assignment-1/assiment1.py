#store student score
student={

    101:{ "Name": "Aditya","scores": [75,85,90]},
    102:{ "Name": "Soham","scores": [55,45,80]},
    103:{ "Name": "rohit","scores": [50,35,20]},
    104:{ "Name": "Abhinav","scores": [70,45,80]},
    105:{ "Name": "pranav","scores": [32,25,20]},

}
#calculatin average and flag pass/faile
for sid,details in student.items():
    avg=sum(details["scores"])/len(details["scores"])
    details["avrage"]=avg
    details["passed"]=avg>=50 #boolean flag
    details["failed"]=avg<=49

#print namesw of student who passed

for sid,details in student.items():

    if details["passed"]== True:

        print(details["Name"]," is passed")
    elif details["failed"]==True:
       
        print(details["Name"],"is failed")

