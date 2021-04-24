n=int(input('Enter:'))
l=len(str(n))
temp=n
s=0
while temp>0:
    dig=temp%10
    s+=dig**l
    temp//=10
if s==n:
    print('Armstrong')
else:
    print('No')