def occurence(str):
    d={}
    for i in str:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    return d
str=input("enter a string : ")
print(occurence(str))