n=int(input("enter the number of students passed jee : "))
m=int(input("enter the number of students passed neet : "))
jee=[]
for i in range (n):
    name=input("enter the name of jee passes : ")
    jee.append(name)
neet=[]
for j in range(m):
    name1=input("enter names of neet paseesd : ")
    neet.append(name1)
both=[]
for k in jee: 
    if k in neet:
        both.append(k)
jeeonly=[]
for l in jee:
    if l not in neet:
        jeeonly.append(l)
neetonly=[]
for o in neet:
    if o not in jee:
        neetonly.append(o)
atleast=[]
for p in jee+neet:
    if p not in atleast:
        atleast.append(p)
print("the students passed jee: ",jee)
print("the students passed neet : ",neet)
print("the students passed only jee : ",jeeonly)
print("the students passsed only neet : ",neetonly)
print("the students passed in both : ",both)
print("the students passed in atleast one : ",atleast)

