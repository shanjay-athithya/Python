l=[(54,2),(34,55),(222,223),(12,45),(78,)]
n=int(input("enter the no of digits : "))
l1=[]
for i in l:
    s=0
    for j in i:
        if len(i)==1:
            if len(str(j))==n:
                s+=2
        elif len(str(j))==n:
            s+=1
    if s==2:
        l1.append(i)
print(l1)