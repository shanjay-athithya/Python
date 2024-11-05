n=int(input("enter the number of persons: "))
l1=[]
l2=[]
for i in range(n):
    key=input("enter the student name : ")
    value=int(input("enter the age :"))
    l1.append(key)
    l2.append(value)
d=dict(zip(l1,l2))
print(d)