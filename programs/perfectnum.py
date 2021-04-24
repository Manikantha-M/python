n=int(input('Enter:'))
if n>0:
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if s==n:
        print('Perfect number')
    else:
        print('No')
else:
    print('No')