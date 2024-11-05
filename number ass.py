while True:
    n=int(input("enter a number : "))
    if n>=0:
        break
len=len(str(n))
if len==1:
    print("it is numerically increasing")
while True:
    piece=int(input("enter number of digits in each piece : "))
    if len%piece==0:
        break
div=10**piece
l=[]
if len==piece:
    l.append(n)
else:
    while n>0:
        r=n%div
        l.append(r)
        n=n//div
rev = l[::-1]
sortedl=sorted(rev)
print("the splited list is : ",rev)
if sortedl==rev:
    print("the pieces are in increasing order")
else:
    print("the pieces are not in increasing order")