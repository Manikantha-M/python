n=int(input('Enter:'))
if n>0:
    temp=n
    s=0
    while temp>0:
        dig=temp%10
        fact=1
        for i in range(1,dig+1):
            fact=fact*i
        s+=fact
        temp//=10
    if s==n:
        print('Strong num')
    else:
        print('No')
else:
    print('No')



# def fact(k):
#     if k==0:
#         return 1
#     else:
#         return k*fact(k-1)

# n=int(input('Enter:'))
# if n>0:
#     temp=n
#     s=0
#     while temp>0:
#         dig=temp%10
#         s+=fact(dig)
#         temp//=10
#     if s==n:
#         print('Strong num')
#     else:
#         print('No')
# else:
#     print('No')
