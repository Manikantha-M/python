class Superclass1:

    def super1(self):
        print('super1 method called')

class Superclass2:

    def super2(self):
        print('super2 method called')
        

class Childclass(Superclass1,Superclass2):

    def child(self):
        print('child method called')


c=Childclass()
c.super1()
c.super2()
c.child()