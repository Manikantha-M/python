x=[[12,7],[4,5],[3,8]]
res=[[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        res[j][i]=x[i][j]
for r in res:
    for k in r:
        print(k,end=' ')
    print()