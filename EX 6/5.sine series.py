def sine_series(n,x):
    sum=0
    sign=1
    for i in range(1,2*n-2,2):
        pi=22/7
        rad=x*(pi/180)
        value=sign*((rad**i)/factorial(i))
        sum=sum+value
        sign=sign*-1
    return sum
def factorial(i):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    return fact
n=int(input("enter the number of terms : "))
x=int(input("enter the value of x: "))
print(sine_series(n,x))



