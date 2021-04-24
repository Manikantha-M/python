def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

l=list(map(int,input().split()))
n1=l[0]
n2=l[1]
hcf=gcd(n1,n2)
for i in range(2,len(l)):
    hcf=gcd(hcf,l[i])
print(hcf)