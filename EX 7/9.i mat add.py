def add_mat(m1,m2):
    c=[[0,0],[0,0]]
    for i in range(len(m1)):
        for j in range(len(m1)):
            c[i][j]=m1[i][j]+m2[i][j]
    return c
m1=[[1,2],[2,3]]
m2=[[1,3],[3,4]]
print(add_mat(m1,m2))