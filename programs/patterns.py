# n=int(input('Enter:'))
# for i in range(1,n+1):
#     for j in range(i):
#         print('*',end=' ')
#     print()


# n=int(input('Enter:'))
# for i in range(n,0,-1):
#     for j in range(i):
#         print('*',end=' ')
#     print()


# n=int(input('Enter:'))
# k=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(k,end=' ')
#         k+=1
#     print()


# a='python'
# l=len(a)
# for i in range(1,l+1):
#     for j in range(i):
#         print(a[j],end=' ')
#     print()


# n=int(input('Enter:'))
# k=1
# while k<=n:
#     for i in range(n-k,0,-1):
#         print(' ',end='')
#     for j in range(k):
#         print('*',end=' ')
#     k+=1
#     print()


n=int(input('Enter:'))
k=0
while k<n:
    for i in range(k):
        print(' ',end='')
    for j in range(n-k):
        print('*',end=' ')
    k+=1
    print()