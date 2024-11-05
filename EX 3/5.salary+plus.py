s=int(input("enter the salary: "))
g=input("enter the gender: ")
if (g=="male"):
    if (s<10000):
        b=(0.07*s)
        print("salary is: ",b+s)
    else:
        b=(0.05*s)
        print("salary is: ",b+s)
elif (g=="female"):
    if (s<10000):
        b=(0.17*s)
        print("salary is: ",b+s)
    else:
        b=(0.15*s)
        print("salary is: ",b+s)
        