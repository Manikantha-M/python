lower=int(input('lower:'))
upper=int(input('upper:'))
for num in range(lower,upper+1):
    if num>0:
        s=0
        for i in range(1,num):
            if num%i==0:
                s+=i
        if s==num:
            print(num,end=' ')