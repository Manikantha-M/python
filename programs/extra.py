# a=5
# print('%.6f'%a)


## .format ##
# Multiplication table #

n,r=map(int,input().split())
for i in range(1,r+1):
    print('{0}*{1}={2}'.format(n,i,n*i))