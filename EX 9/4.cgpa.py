def cgpa_stud():
    for stud,gpa in d.items():
        cgpa=sum(gpa)/len(gpa)
        d[stud]=cgpa
    return d
def display_names():
    sortnames=sorted(d.items(),key=lambda x: x[0])
    return sortnames
def display_grade():
    sortgrade=sorted(d.values(),key=lambda x: x[1],reverse=True)
    return sortgrade
d={'sun':[9.9,8.9],'moon':[7.9,9.0],'lily':[6.7,9.1]}
grade=display_grade()
print(dict(cgpa_stud()))
print(dict(display_names()))
print(dict(grade))


