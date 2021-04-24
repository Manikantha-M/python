d1={'george':24,'tom':32}
print(d1)
d={}
d['george']=24
d['tom']=32
d['jenny']=16
print(d)
print(d['george'])
d['jenny']=20
print(d)
d[10]=100
print(d)

for key,value in d.items():
    print(key,':',value)

k={'a':1,'b':2,'c':3,50:500}
print(k)
for i,j in k.items():
    print(i,':',j)