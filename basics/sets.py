a=set()
print(a,type(a))
a.add(1)
a.add(2)
print(a)
for i in a:
    print(i)

b=set([11,22,33])
print(b)
for x in b:
    print(x)

b=[1,1,2,4,2]
s1=set()
for i in b:
    s1.add(i)
print(s1)
s2=set(b)
print(s2)

l=[]
for i in s1:
    l.append(i)
print(l)

l1=list(s2)
print(l1)

c=set()
c.add('apple')
c.add('banana')
c.add(1)
print(c)

l2=[1,3,4,1,3]
s3=set()
for i in l2:
    s3.add(i)
print(s3)
sum1=0
for i in s3:
    sum1+=i
print(sum1)
print(sum(s3))