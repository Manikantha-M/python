r,c=map(int,input().split())
sp1=input()
res=[]
for i in range(r):
    row=[]
    for j in range(c):
        row.append(0)
    res.append(row)

x=[]
y=[]
for m in range(r):
    x.append(list(map(int,input().split())))
sp2=input()
for n in range(r):
    y.append(list(map(int,input().split())))

for i in range(len(x)):
    for j in range(len(x[0])):
        res[i][j]=x[i][j]+y[i][j]

print()
for r1 in res:
    for k in r1:
        print(k,end=' ')
    print()


