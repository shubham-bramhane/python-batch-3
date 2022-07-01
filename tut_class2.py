# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         area_circle=3.14*self.radius*self.radius
#         print('area of circle',area_circle)


#     def perimeter(self):
#         peri=2*3.14*self.radius
#         print('perimeter of circle',peri)

#     def volume(self):
#         volume=(4/3)*3.14*self.radius*self.radius*self.radius

#         print('volume of circle',volume)



# obj=Circle(14)
# obj.area()
# obj.perimeter()
# obj.volume()




# obj2=Circle(20)
# obj2.area()
# obj2.perimeter()
# obj2.volume()



class Parent():    # parent classs

    def __init__(self,radius):
        self.radius=radius

    def details(self):
        print('parent class radius',self.radius)


class Child(Parent):
    def __init__(self, radius,length):
        super().__init__(radius)
        self.length=length

    def details2(self):
        print('length=',self.length)
        return super().details()




class grand(Child):
    def __init__(self, radius, length,breadth):
        super().__init__(radius, length)
        self.breadth=breadth

    def details3(self):
        print('breadth value=',self.breadth)
        return super().details2()

obj=grand(10,12,13)
obj.details3()


