def edit(f):
    uc=0
    lc=0
    nc=0
    word=f.read()
    for ch in word:
        if ch.isupper():
            uc+=1
        elif ch.islower():
            lc+=1
        elif ch.isnumeric():
            nc+=1
    print("the no of uppercase is : ",uc)
    print("the no of lowercase is : ",lc)
    print("the no of numeric is : ",nc)
f=open("t1.txt","r+")
edit(f)