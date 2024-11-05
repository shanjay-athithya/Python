def mat_transpose(m):
    mt=[[0,0,0],[0,0,0],[0,0,0]]
    if len(m)==len(m[0]):
        for i in range(len(m)):
            for j in range(len(m)):
                mt[j][i]=m[i][j]
    return mt
m=[[1,2,3],[4,5,6],[7,8,9]]           
print(mat_transpose(m))