n=int(input("enter the number of lines= "))
for lines in range(1,n+1):
    for rows in range(lines,0,-1):
        print(rows,end="")
    print()