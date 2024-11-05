a=int(input("enter mark 1: "))
b=int(input("enter mark 2: "))
c=int(input("enter mark 3: "))
d=int(input("enter mark 4: "))
e=int(input("enter mark 5: "))
ave=(a+b+c+d+e)//5
if (90<=ave<=100):
    print("distinction")
elif (80<=ave<90):
    print("First class")
elif (70<=ave<80):
    print("Second class")
elif (60<=ave<70):
    print("Third class")
else:
    print("fail")
