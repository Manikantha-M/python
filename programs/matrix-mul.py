x=[[12,7,3],[4,5,6],[7,8,9]]
y=[[5,8,1,2],[6,7,3,0],[4,5,9,1]]
res=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            res[i][j]+=x[i][k]*y[k][j]

for r in res:
    for k in r:
        print(k,end=' ')
    print()