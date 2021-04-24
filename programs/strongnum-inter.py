lower=int(input('lower:'))
upper=int(input('upper:'))
for num in range(lower,upper+1):
    if num>0:
        temp=num
        s=0
        while temp>0:
            fact=1
            dig=temp%10
            for i in range(1,dig+1):
                fact=fact*i
            s+=fact
            temp//=10
        if s==num:
            print(s,end=' ')