def remcom(f,f1):
    s=f.readlines()
    for l in s:
        word=l.split(" ")
        for w in word:
            for ch in w:
                if ch=="#":
                    break
                else:
                    f1.write(ch)
            f1.write(" ")
        f1.write("\n")
f=open("code.txt","r")
f1=open("recordcode.txt","a")
remcom(f,f1)
    






