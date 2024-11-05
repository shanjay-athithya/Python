n=int(input("enter the lenght of tuple to be  removed : "))
list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
for i in list:
    if len(i)==n:
        list.remove(i)
print(list)