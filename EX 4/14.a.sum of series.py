n=int(input("enter the number of terms: "))
x=int(input("enter the value of x: "))
sum=1
for i in range(2,n+1):
    sum+=(x**i)/i
print("the answer is : ",sum)