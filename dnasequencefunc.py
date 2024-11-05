def add1(species1,index):
    l1=list(species1)
    l1.insert(index,indel)
    str1=''.join(l1)
    return str1
def add2(species2,index):
    l1=list(species2)
    l1.insert(index,indel)
    str1=''.join(l1)
    return str1
def del1(species1,index):
    l2=list(species1)
    l2.pop(index)
    str2=''.join(l2)
    return str2
def del2(species2,index):
    l2=list(species2)
    l2.pop(index)
    str2=''.join(l2)
    return str2
def scoring(species1,species2):
    if option == "s":
        len1 = len(species1)
        len2 = len(species2)
        matches=0
        mismatches=0
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
                    matches=+1
                    l31.append(species1[i].lower())
                    l32.append(species2[i].lower())
                else:
                    mismatches+=1
                    l31.append(species1[i].upper())
                    l32.append(species2[i].upper())
            str31=''.join(l31)
            species1=str31
            print(str31)
            str32=''.join(l32)
            species2=str32
            print(str32)
        if len2>len1:
            l4=list(species1)
            for i in range (len2-len1):
                l4.append("-")
                str4=''.join(l4)
                species1=str4
            l41=[]
            l42=[]
            for i in range(len(species1)):
                if species1[i]==species2[i]:
                    matches+=1
                    l41.append(species1[i].lower())
                    l42.append(species2[i].lower())
                else:
                    mismatches+=1
                    l41.append(species1[i].upper())
                    l42.append(species2[i].upper())
            str41=''.join(l41)
            species1=str41
            print(str41)
            str42=''.join(l42)
            species2=str42
            print(str42)      
        if len1==len2:
            l51=[]
            l52=[]
            for i in range(len(species1)):
                if species1[i]==species2[i]:
                    matches+=1
                    l51.append(species1[i].lower())
                    l52.append(species2[i].lower())
                else:
                    mismatches+=1
                    l51.append(species1[i].upper())
                    l52.append(species2[i].upper())
            str51=''.join(l51)
            print(str51)
            species1=str51
            str52=''.join(l52)
            species2=str52
            print(str52)
        print("the number of matches : ",matches)
        print("the number of mismatches : ",mismatches)
species1=input("enter dna seq 1 : " )
species2=input("enter dna seq 2 : ")
indel="-"
while True:
    print("""choose any one of the options:
    1.enter "a" for adding an indel
    2.enter "d" for deleting an indel
    3.enter "s" for scoring the present alignment
    4.enter "q" for quiting """)
    option=input("enter an option : ")
    if option=="a":
        string=input("enter the SEQUENCE needed to be changed (1 or 2): ")
        index=int(input("enter the index number at which it has to be inserted : "))
        if string== "1":
            if index>=len(species1):
                print("index not in range")
            else:
                str1=add1(species1,index)
                print(str1)
                species1=str1
        elif string=="2":
            if index>=len(species2):
                print("index not in range")
            else:
                str1=add2(species2,index)
                print(str1)
                species2=str1
    if option=="d":
        string=input("enter the SEQUENCE needed to be changed (1 or 2) : ")
        index=int(input("enter the index number at which the indel has to be deleted : "))       
        if string=="1":
            if species1[index]!="-":
                print("indel not found in sequence")
            else:
                str2=del1(species1,index)
                print(str2)
                species1=str2
        elif string=="2":
            if species2[index]!="-":
                print("indel not found in sequence")
            else:
                str2=del2(species2,index)
                print(str2)
                species2=str2
    if option == "s":
        print(scoring(species1,species2))
    if option== "q":
        print("DNA editing is quited")
        break
