str=input("entre a string: ")
delete=input("enter the character which needs to be deleted: ")
for i in str:
    if i==delete:
        continue
    print(i,end="")