n=int(input("enter the number: "))
i=eval(input("enter tolerence: "))
x=n
count=0
while True:
    count+=1
    root=0.5*(x+(n/x))
    if (abs(root-x)<i):
        break
    x=root
print("the square root is :",root)