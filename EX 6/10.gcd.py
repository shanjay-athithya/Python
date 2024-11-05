def gcd(a,b):
    if a>b:
        if b==0:
            return a
        else:
            return gcd(b,a%b)
    else:
        if a==0:
            return b
        else:
            return gcd(a,b%a)
a=int(input("enter num 1 : "))
b=int(input("enter num 2 : "))
print(gcd(a,b))