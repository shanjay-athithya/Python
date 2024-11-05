def div(piece):
    return 10**piece
def split(n):
    l=[]
    if len==piece:
        l.append(n)
        return l
    else:
        while n>0:
            r=n%div
            l.append(r)
            n=n//div
        return l
def checking(rev,sortedlist):
    if rev==sortedlist:
        print("the pieces are in increasing order")
    else:
        print("the pieces are not in increasing order")
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
div=div(piece)
l=split(n)
rev = l[::-1]
sortedlist=sorted(rev)
print("the splited list is : ",rev)
print(checking(rev,sortedlist))


