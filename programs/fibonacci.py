n=int(input('Enter:'))
a=0
b=1
if n==1:
    print(a)
else:
    print(a,end=' ')
    print(b,end=' ')
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        print(c,end=' ')