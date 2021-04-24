class A:

    def m1(self):
        print('m1 from A')
    
class B(A):

    def m1(self):
        print('m1 from B')
    

c=B()
c.m1()