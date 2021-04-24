a=[1,3,5,7,9,11]
c=[]
for i in a:
    c.append(2*i)
print(c)

d=[i*2 for i in a]
print(d)

e=[]
for i in range(1,7):
    e.append(i**2)
print(e)

e2=[i**2 for i in range(1,7)]
print(e2)

f=[i**2 for i in range(6,0,-1)]
print(f)