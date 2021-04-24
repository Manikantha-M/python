# for i in range(1,10,2):
#     print(i)

# i=1
# while i<=10:
#     if i%2==0:
#         i+=1
#         continue
#     else:
#         print(i,end=' ')
#         i+=1

# print(pow(2,3))

# print(type('abc'))
# print(type(4))
# print(type(True))
# print(type(False))

# a=3
# b=1
# if a>b:
#     print('a is greater than b')

# a=3
# b=10
# if True:
#     print('a is greater than b')


a=3
b=1
if a>b:
    print('a is greater than b')

bool_val=a>b
print(bool_val)

if bool_val:
    print('a is greater than b')

def ru_sad(is_rainy,has_umbrella):
    if is_rainy==True and has_umbrella==False:
        return True
    else:
        return False

print(ru_sad(True,False))
print(ru_sad(False,False))