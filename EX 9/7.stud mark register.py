d={1:{"maths":{98,99,100},"physics":{90,91,89},"python":{95,96,98}},
2:{"maths":{100,99,90},"physics":{90,94,89},"python":{95,98,98}},
3:{"maths":{98,90,100},"physics":{90,88,89},"python":{95,96,88}}}
print("the dictionary is : ",d)
reg=int(input("enter your reg number : "))
print("the stud info from reg no is : ",d[reg])
reg1=int(input("enter your reg number : "))
sub=input("enter subject code : ")
print("the stud info from reg no is ",d[reg1][sub])
reg3=int(input("enter your reg number : "))
subj=input("enter the subject code to be changed : ")
marks=input("enter the dictonary of marks : ")
d[reg3][subj]=marks
print("the updated stud info is : ")
print(d[reg3][subj])