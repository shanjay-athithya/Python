def keyfinder(f):
    import keyword
    word=f.read()
    for w in word.split():
        if keyword.iskeyword(w):
            print(w,end=",")
f=open("code.txt","r")
print("the weywords are: ")
print(keyfinder(f))