"""def findall(f):
    d={}
    s=f.read()
    word=s.split(" ")
    nxt=word.split("/n")
    for w in nxt:
        if w not in d:
            d[w]=1
        else:
            d[w]=d[w]+1
    return d
f=open("ebook.txt","r")
print(findall(f))"""

def findall(f):
    d={}
    s=f.read()
    lines=s.split("\n")
    for l in lines:
        word=l.split(" ")
        for w in word:
            if w not in d:
                d[w]=1
            else:
                d[w]=d[w]+1
    return d
f=open("ebook.txt","r")
print(findall(f))
