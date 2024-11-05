u=int(input("number of units current used: "))
if (u<=500):
    bill=u*1.5
    print("the bill is: ",bill)
elif (500<u<=1000):
    bill=(750+(u-500)*3)
    print("the bill is: ",bill)
else:
    bill=(2250+(u-1000)*5)
    print("the bill is: ",bill)