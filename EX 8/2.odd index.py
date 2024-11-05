t = (1, 3, 2, 4, 6, 5)
l=list(t)
l1=[]
for i in range (1,len(l),2):
    l1.append(l[i])
print(tuple(l1))
