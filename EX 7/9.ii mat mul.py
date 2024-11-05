def mul_mat(m1,m2):
    c=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for x in range(len(m2)):
                c[i][j]+=m1[i][x]*m2[x][j]
    return c
m1=[[1,2,3],[1,3,2],[1,1,1]]
m2=[[2,3,4],[1,2,3],[3,2,1]]      
print(mul_mat(m1,m2))      
