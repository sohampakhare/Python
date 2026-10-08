#store student score
student={

    101:{ "Name": "Aditya","scores": [75,85,90]},
    102:{ "Name": "Soham","scores": [55,45,80]},
    103:{ "Name": "rohit","scores": [50,35,20]},

}
#calculatin average and flag pass/faile
for sid,details in student.items():
    avg=sum(details["scores"])/len(details["scores"])
    details["avrage"]=avg
    details["passed"]=avg>=50 #boolean flag

#print namesw of student who passed
print("student who passsed")
for sid,details in student.items():
    if details["passed"]== True:
        print(details["Name"])


