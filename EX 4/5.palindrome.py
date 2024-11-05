n=int(input("enter the number: "))
s=0
temp=n
while(n>0):
    r=n%10
    s=10*s+r
    n=n//10
if (s==temp):
    print("paalindrome")
else:
    print("not a palinndrome")