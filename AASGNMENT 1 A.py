species1=input("enter the DNA sequence 1: ")
species2=input("enter the DNA sequence 2: ")
indel="-"
while True:
    print("""choose any one of the options:
    1.enter "a" for adding an indel
    2.enter "d" for deleting an indel
    3.enter "s" for scoring the present alignment
    4.enter "q" for quiting """)
    option=input("enter an option : ")
    if option=="a":
        string=input("enter the SEQUENCE needed to be changed : ")
        index=int(input("enter the index number at which it has to be inserted : "))

        if string== "1":
            l1=list(species1)
            l1.insert(index,indel)
            str1=''.join(l1)
            species1=str1
            print(species1)
        else:
            l1=list(species2)
            l1.insert(index,indel)
            str1=''.join(l1)
            species2=str1
            print(species2)
    if option=="d":
        string=input("enter the SEQUENCE needed to be changed  : ")
        index=int(input("enter the index number at which the indel has to be deleted : "))
        l2=list(string)
        l2.pop(index)
        str2=''.join(l2)
        if string==species1:
            species1=str2
            print(species1)
        else:
            species2=str2
            print(species2)
    if option == "s":
        len1 = len(species1)
        len2 = len(species2)
        if len1>len2:
            l3=list(species2)
            for i in range (len1-len2):
                l3.append("-")
                str3=''.join(l3)
                species2=str3
                l31=[]
                l32=[]
            for i in range(len(species2)):
                if species1[i]==species2[i]:
                    l31.append(species1[i].lower())
                    l32.append(species2[i].lower())
                else:
                    l31.append(species1[i].upper())
                    l32.append(species2[i].upper())
            str31=''.join(l31) 
            print(str31)
            str32=''.join(l32)
            print(str32)
        if len2>len1:
            l4=list(species1)
            for i in range (len2-len1):
                l4.append("-")
                str4=''.join(l4)
                species1=str4
                print(species1)
            l41=[]
            l42=[]
            for i in range(len(species1)):
                if species1[i]==species2[i]:
                    l41.append(species1[i].lower())
                    l42.append(species2[i].lower())
                else:
                    l41.append(species1[i].upper())
                    l41.append(species2[i].upper())
            str41=''.join(l41)
            print(str41)
            str42=''.join(l42)
            print(str42)
    if option== "q":
        print("DNA editing is quited")
        break