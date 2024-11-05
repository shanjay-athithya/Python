string=input("enter a string: ")
upper=0
lower=0
numeric=0
spl=0
for i in string:
    if(i.islower()):
        lower=lower+1
    elif (i.isupper()):
        upper=upper+1
    elif (i.isnumeric()):
        numeric=numeric+1
    else:
        spl=spl+1
print("number of lower case= ",lower)
print("number of upper case= ",upper)
print("number of numeric values= ",numeric)   
print("number of special characters= ",spl)