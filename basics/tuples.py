t=()
t1=(11,22,33)
print(t,type(t))
print(t1,type(t1))

t2=tuple([1,2,3,4])
print(t2)

t3=tuple('abc')
print(t3)
print(t3[0])

t4=(1,12,55,12,81)
print(min(t4))
print(max(t4))
print(sum(t4))
print(len(t4))

t5=(11,22,33,44,55)
for i in t5:
    print(i)