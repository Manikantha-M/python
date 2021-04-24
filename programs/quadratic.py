import cmath
a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))
disc=cmath.sqrt(b**2 - 4*a*c)
sol1=(-b+disc)/(2*a)
sol2=(-b-disc)/(2*a)
print(round(sol1.real,3)+round(sol1.imag,3)*1j)
print(round(sol2.real,3)+round(sol2.imag,3)*1j)