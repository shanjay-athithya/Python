n=int(input("enter the number: "))
count=len(str(n))
temp=n
sum=0
while(n>0):
    r=n%10
    sum=sum+r**count
    n=n//10
print(sum)
if(temp==sum):
    print("amstrong number")
else:
    print("not a amstrong")
