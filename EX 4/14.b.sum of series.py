n=int(input("enter the number of terms :"))
x=int(input("enter the value of x: "))
sum=0
count=-1
for i in range(1,n+1):
    sum+=count*(x**i)
    count*=-1
print("the value is : ",sum)