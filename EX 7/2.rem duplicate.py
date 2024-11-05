l=[]
def rem_dup(list):
    for element in list:
        if element not in l:
            l.append(element)
    return l
import random as r
list=[]
for i in range(1,11):
    element=r.randint(0,6)
    list.append(element)
print("the random generated list is: ")
print(list)
print("the updated list is: ")
print(rem_dup(list))
