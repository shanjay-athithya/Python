str=input("enter a string: ")
#converting string to a list 
char=list(str)
#.sort() used to arrrange in ascending order
char.sort()
#.join() used to convert the list to string
print("".join(char))