import random
# n=int(input('length:'))
# a=[]
# for i in range(n):
#     a.append(random.randint(1,8))
# print(a)


n=int(input('length:'))
a=[]
for i in range(n):
    a.append(random.randrange(1,20,2))
print(a)