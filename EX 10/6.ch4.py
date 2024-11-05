def display_letters(f):
    l=[]
    s=f.read()
    word=s.split(" ")
    for i in word:
        if len(i)<4:
            l.append(i)
    return l
f=open("ebook.txt","r")
print("the words less than 4 characters are :")
print(display_letters(f))