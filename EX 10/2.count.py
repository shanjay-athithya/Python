def assignment_analyser(f):
    cl=0
    cw=0
    cc=0
    rl=f.read()
    lines=rl.split("\n")
    for i in lines:
        cl+=1
        w=i.split(" ")
        for word in w:
            cw+=1
            for ch in word:
                cc+=1
    print("the no of lines :",cl)
    print("the number of words: ",cw)
    print("the number of characters:",cc)
f=open("assignment.txt","r")
print(assignment_analyser(f))



