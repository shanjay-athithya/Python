for n in range(2,101):
    count=0
    for i in range(2,n):
        if (n%i==0):
            count=count+1
            break
    if (count==0):
        print(n)
    
 



