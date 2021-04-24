lower=int(input('lower:'))
upper=int(input('upper:'))
for num in range(lower,upper+1):
    temp=num
    l=len(str(num))
    s=0
    while temp>0:
        dig=temp%10
        s+=dig**l
        temp//=10
    if s==num:
        print(s,end=' ')
