l=[]
for i in range(1,11):
    name=input("enter the name : ")
    l.append(name)
print(l)
search=input("enter the element to search: ")
for i in l:
    if search==i:
        print(search,"is present")
    if search not in l:
        print("not found")
sort=sorted(l)
print("the sorted list : ",sort)
low=0
high=len(sort)-1
b=input("enter element to search : ")
while low<=high:
    mid=(low+high)//2
    if sort[mid]<b:
        low=mid+1
    elif sort[mid]>b:
        high=mid-1
    else:
        print("the binary search is done and element is found at index : ",mid)
        break
else:
    print("not found")