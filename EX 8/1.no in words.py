def words(i):
    if i== 1:
        return 'one'
    elif i==2:
        return 'two'
    elif i==3:
        return 'three'
    elif i==4:
        return 'four'
    elif i==5:
        return 'five'
    elif i==6:
        return 'six'
    elif i==7:
        return 'seven'
    elif i==8:
        return 'eight'
    elif i==9:
        return 'nine'
    elif 1==0:
        return 'zero'
l=[]
n=int(input("enter the number : "))
while n>0:
    i=n%10
    word=words(i)
    l.append(word)
    n=n//10
sortedl=l[::-1]
print(tuple(sortedl))