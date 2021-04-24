# n=int(input('Enter:'))
# print('binary',bin(n))
# print('octal',oct(n))
# print('hexa',hex(n))

# n=int(input('Enter:'))
# if n>0:
#     bin=''
#     while n>0:
#         rem=n%2
#         bin=str(rem)+bin
#         n//=2
#     print(bin)
# else:
#     print(0)


n=int(input('Enter:'))
if n>0:
    oct=''
    while n>0:
        rem=n%8
        oct=str(rem)+oct
        n//=8
    print(oct)
else:
    print(0)
