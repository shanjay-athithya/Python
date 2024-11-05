def sort_studentname(f,f1):
    s=f.readlines()
    sort=sorted(s)
    for i in sort:
        f1.write(i)
f=open("student.txt","r")
f1=open("sortstudent.txt","w")
sort_studentname(f,f1)
