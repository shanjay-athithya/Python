def separation(n):
    while (n>0):
        global r
        r=n%10
        primefinder(r)
        n=n//10
def primefinder(r):
    l=[2,3,5,7]
    if r in l:
        print(r,"is a prime number")
n=int(input("enter a number"))
print(separation(n))
