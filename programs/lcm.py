def lcm(x,y):
    if x>y:
        x,y=y,x
    for i in range(y,(x*y)+1,y):
        if i%x==0:
            return i

x,y=map(int,input().split())
res=lcm(x,y)
print(res)