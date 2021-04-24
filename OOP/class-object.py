class Person:
    
    def __init__(self,name):
        self.name=name
    
    def whoami(self):
        return 'You are '+self.name


p1=Person('tom')
print(p1.name)
print(p1.whoami())

p1.name='jerry'
print(p1.name)
print(p1.whoami())