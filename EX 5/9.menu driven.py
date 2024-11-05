#menu type program
print("""the options are:
1.first occurence of a substring.
2.right justify a string.
3.capitalize the first letter of a string.
4.check whether tthe string is alpannumeric
5.partion the given text into three parts.""")
str=input("enter the string : ")
substr=input("enter the substring :")
ch=int(input("enter an option : "))
if ch==1:
    print(str.rfind(substr))
elif ch==2:
    print(str.rjust(len(str)+3,"*"))
elif ch==3:
    print(str.capitalize())
elif ch==4:
    print(str.isalnum())
elif ch==5:
    print(str.partition(substr))