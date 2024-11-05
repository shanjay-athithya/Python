def find_sum_even(n):
    sum=0
    for i in range(0,n+1,2):
        sum=sum+i
    return sum
n=int(input("enter the range : "))
print(find_sum_even(n))