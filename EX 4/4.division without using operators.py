a=int(input("enter divident : "))
b=int(input("enter divisor : "))
count=0
while count<a:
    count+=1
    factor=b*count
    if factor==a:
        print("the quotient is : ",count)
        print("the remainder is : 0")
        break
    elif factor>a:
        count-=1
        rem=a-(b*count)
        print("the quotient is : ",count)
        print("the remainder is : ",rem)
        break
