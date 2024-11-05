def occurence(string):
    d={}
    for i in string:
        c=0
        for j in string:
            if i==j:
                c=c+1
        d[i]=c
    return d
string=input("enter a string : ")
print("the dictionary for no of occurences is  : ",occurence(string))
