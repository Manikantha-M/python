def lcm(x,y):
    if x>y:
        x,y=y,x
    for i in range(y,(x*y)+1,y):
        if i%x==0:
            return i

l=list(map(int,input().split()))
n1=l[0]
n2=l[1]
lcmf=lcm(n1,n2)
for i in range(2,len(l)):
    lcmf=lcm(lcmf,l[i])
print(lcmf)