d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400} 
d3={}
for i,j in d1.items():
    if i in d2:
        d3[i]=d1[i]+d2[i]
    if i not in d2.values():
        d3[i]=d1[i]
for i,j in d2.items():
    if i not in d3:
        d3[i]=d2[i]
print("the new dictionary is : ",d3)
print("the keys are : ",d3.keys())
print("the values are : ",d3.values())
print("the items are : ",d3.items())
