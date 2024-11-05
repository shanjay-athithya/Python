def rem_dup(glst):
    new_list=[]
    for i in glst:
        if i not in new_list:
            new_list.append(i)
    print('updated list:')
    return new_list
import random as r
glst=[]
for i in range(0,10):
    x=r.randint(0,6)
    glst.append(x)
print("random number list:",glst)
print(rem_dup(glst))