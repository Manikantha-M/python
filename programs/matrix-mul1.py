r1,c1=map(int,input().split())
r2,c2=map(int,input().split())
sp1=input()
res=[]
for i in range(r1):
    row=[]
    for j in range(c2):
        row.append(0)
    res.append(row)
x=[]
y=[]
for m in range(r1):
    x.append(list(map(int,input().split())))
sp2=input()
for n in range(r2):
    y.append(list(map(int,input().split())))

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            res[i][j]+=x[i][k]*y[k][j]

print()
for r in res:
    for k in r:
        print(k,end=' ')
    print()