n=int(input("enter the range of list: "))
lst=[]
for i  in range(n):
    ele=int(input("enter the element : "))
    lst.append(ele)
print("the list is : ",lst)
def print_reversed(lst):
    for j in range(n//2):
        b=lst[j]
        lst[j]=lst[n-j-1]
        lst[n-j-1]=b
    print("the reversed list is : ",lst)
print(print_reversed(lst))


