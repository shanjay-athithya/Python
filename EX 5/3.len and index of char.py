string=input("enter a string: ")
length=len(string)
print("length of string : ",length)
count=0
for i in string:
    print(i,"=",count)
    count=count+1