n=int(input("year: "))
if (n%400==0):
    print("leap")
elif (n%4==0) and (n%100!=0):
    print('leap')
else:
    print("not leap")