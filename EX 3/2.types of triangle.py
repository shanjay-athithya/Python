a=int(input("enter side 1: "))
b=int(input("enter side 2: "))
c=int(input("enter side 3: "))
if a==b:
    if b==c:
        print("equalateral triangle")
    else:
        print("isoceles triangle")
else:
    if b==c:
        print("isoceles triangle")
    else:
        print("scalar triangle")