n=int(input("enter the number of names: "))
l=[]
for i in range(n):
    name=input("enter  name : ")
    l.append(name)
count=0
for i in l:
    for j in i:
        if j=="a":
            count+=1
print("number of times 'a' occured :",count)
