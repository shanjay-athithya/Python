tup=(1,2,2,1,3,5,6,7,4,2,5)
l1=list(tup)
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(tuple(l2))


