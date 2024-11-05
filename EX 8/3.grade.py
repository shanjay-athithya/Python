mark_list=[('Rams',120,55,45,65,45,32),('Vel',121,94,86,78,67,90), ('Siri',122,73,98,90,87,89)]
def garde(sum):
    ave=sum/5
    if (ave>=90):
        return 'A'
    elif (80<=ave<90):
        return 'B'
    elif (65<ave<80):
        return 'C'
    elif (40<=ave<=65):
        return 'D'
sum=0
mark_list1=[]
for  i in mark_list:
    a=tuple()
    a+=tuple(i[:2])
    for j in range(2,len(i)):
        sum+=i[j]
    a=a+tuple([garde(sum)])
    mark_list1.append(a)
print(mark_list1)