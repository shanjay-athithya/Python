a=int(input("ENTRER:"))
f=[]
s=int(input("enter no:"))
if len(str(a))%s!=0:
    f.append(a)
else:
    while a!=0:
        f.append(a%(10**s))
        a=a//(10**s)
f1=[]
for i in range(-1,-len(f)-1,-1):
    f1.append(f[i])
print(f1)
l=f1.sort()