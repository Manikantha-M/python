# import math
# class Circle:

#     def __init__(self,radius):
#         self.__radius=radius
    
#     def setRadius(self,radius):
#         self.__radius=radius

#     def getRadius(self):
#         return self.__radius

#     def area(self):
#         return math.pi * (self.__radius**2)
    
#     def __add__(self,other_circle):
#         return Circle(self.__radius + other_circle.__radius)


# c1=Circle(4)
# print(c1.getRadius())
# c2=Circle(5)
# print(c2.getRadius())
# c3=c1+c2
# print(c3.getRadius())




class Circle:

    def __init__(self,radius):
        self.__radius=radius
    
    def getRadius(self):
        return self.__radius

    ## overload '+' operator ##
    def __add__(self,other_circle):
        return Circle(self.__radius + other_circle.__radius)
    
    ## overload '>' operator ##
    def __gt__(self,other_circle):
        return self.__radius > other_circle.__radius

    ## overload '<' operator ##
    def __lt__(self,other_circle):
        return self.__radius < other_circle.__radius
    
    ## string representation ##
    def __str__(self):
        return 'Circle with radius '+str(self.__radius)


c1=Circle(4)
print(c1.getRadius())
c2=Circle(5)
print(c2.getRadius())
print(c1)
print(c2)
c3=c1+c2
print(c3.getRadius())
print(c3)
print(c3>c2)
print(c2<c1)
