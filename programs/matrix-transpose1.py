r,c=map(int,input().split())
sp1=input()
res=[]
for i in range(c):
    row=[]
    for j in range(r):
        row.append(0)
    res.append(row)
x=[]
for m in range(r):
    x.append(list(map(int,input().split())))


for i in range(len(x)):
    for j in range(len(x[0])):
        res[j][i]=x[i][j]

print()
for r1 in res:
    for k in r1:
        print(k,end=' ')
    print()