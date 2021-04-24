# def sum1(*args):
#     s=0
#     for i in args:
#         s+=i
#     print(s)

# sum1(1,2,3,4)
# sum1(1,2,3,4,5,6,7)


# def myfunc(**kwargs):
#     for i,j in kwargs.items():
#         print(i,j)
#     print(kwargs)

# myfunc(name='tim',sport='football',roll=19)


def three(a,b,c):
    print(a,b,c)
a=[1,2,3]
three(*a)

def keythree(a,b,c):
    print(a,b,c)

a={'a':'one','b':'two','c':'three'}
keythree(**a)