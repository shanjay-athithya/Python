def sum(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n+sum(n-2)
n=int(input("enter the number: "))
print(sum(n))