# a=[5,3,8,6,7,2]
# for i in range(len(a)-1,0,-1):
#     for j in range(i):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

# a=[5,3,8,6,7,2]
# for i in range(len(a)-1,0,-1):
#     for j in range(i):
#         if a[j]<a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

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
#     for i in range(n-k):
#         print(' ',end='')
#     for j in range(k):
#         print('*',end=' ')
#     print()
#     k+=1

n=int(input('Enter:'))
k=1
while k<=n:
    for i in range(k-1):
        print(' ',end='')
    for j in range(n-k+1):
        print('*',end=' ')
    print()
    k+=1