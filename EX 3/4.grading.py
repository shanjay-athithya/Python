a=int(input("enter mark 1: "))
b=int(input("enter mark 2: "))
c=int(input("enter mark 3: "))
ave=(a+b+c)//3
if (90<=ave<=100):
    print("A grade")
elif (80<=ave<90):
    print("B grade")
elif (70<=ave<80):
    print("C grade")
elif (60<=ave<70):
    print("D grade")
else:
    print("E grade")