string=input("enter a string: ")
sub_string=input("enter the substring : ")
count=string.count(sub_string)
if sub_string in string:
    print("no of occurence: ",count)
else:
    print("not found")
index=-1
while True:
    index=string.find(sub_string,index+1)
    if index==-1:
        break
    else:
        print("index of each occurence: ",index)

