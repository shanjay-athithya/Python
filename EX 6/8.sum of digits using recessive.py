def sumDigits(n):
    if n<0:
        return "invalid input"
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (n%10)+sumDigits(n//10)
n=int(input("enter the number : "))
print(sumDigits(n))
