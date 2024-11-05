test_list = [4, 5, 4, 5, 6, 6, 5]
l=[]
dupl=[]
for i in test_list:
    if i not in dupl:
        dupl.append(i)
        count=0
        for j in range(0,len(test_list)):
            if i==test_list[j]:
                count=count+1
        tup=(i,count)
        l.append(tup)
print(l)