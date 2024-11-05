l1 = [1, 'x', 4, 5.6, 'z', 9, 'a', 0, 4]
l2=[]
l2=[i for i in l1 if type(i)==int]
print(l2)
l3=[]
w=input("enter a string : ")
l3=[j for j in w if j not in ["a","e","i","o","u"]]
print(l3)
l4=[]
l4=[str(i)+"a" for i in range(1,5)]
print(l4)
c=[0,0,0]
a=[1,2,3]
b=[4,5,6]
c=[a[i]+b[i] for i in range (len(a))]
print(c)
