n=int(input("enter the number of rows : "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for x in range(0,i):
        print("*",end=" ")
    print()