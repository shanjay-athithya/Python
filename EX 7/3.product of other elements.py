arr=[]
prod_list=[]
def prodlist(arr):
    for j in arr:
        prod=1
        for x in arr:
            if x!=j:
                prod*=x
        prod_list.append(prod)
    return prod_list
n=int(input("enter the range of list: "))
for i in range(n):
    a=int(input("enter the number : "))
    arr.append(a)
print("arr list is :",arr)
print("the product list is : ")
print(prodlist(arr))