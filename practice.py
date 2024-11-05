"""l=[['shanj',12],['harii',4],['kunji',8]]
sort=sorted(l,key=lambda x: x[0])
print(sort)"""

'''test = {'Nikhil' : { 'roll' : 24, 'marks' : 17},
             'Akshat' : {'roll' : 54, 'marks' : 12},
             'Akash' : { 'roll' : 12, 'marks' : 15}}
sort=sorted(test.items(),key=lambda x: x[1]['roll'])
print(sort)
 '''

"""test = {'Nikhil' : { 'roll' : 24, 'marks' : 17},
             'Akshat' : {'roll' : 54, 'marks' : 12},
             'Akash' : { 'roll' : 12, 'marks' : 15}}
search=input("enter item to search : ")
print(test['Nikhil'][search])"""

"""def email():
    name=input("enter name in small letter for email use: ")
    print("""choose the following below :
          1.@gamil.com
          2.@yahoo.com
          3.@hotmail.com
          4.@outlook.com""")
    choice=int(input("enter any choice: "))
    if choice==1:
        print(name+"@gamil.com")
    elif choice==2:
        print(name+"@yahoo.com")
    elif choice==3:
        print(name+"@hotmail.com")
    elif choice==4:
        print(name+"@outlook.com")
email()"""

d={1:{"shan":12,"sar":13},2:{"san":14,"ara":15}}
print(d[1]["sar"])
