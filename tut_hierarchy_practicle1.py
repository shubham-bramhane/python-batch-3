class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def rectangleArea(self):
        print('area of rectanlge is',self.length*self.breadth)


class square():
    def __init__(self,side):
        self.side=side

    def sqaureArea(self):
        print('area of square is ',self.side*self.side)


class Circle():
    def __init__(self,radius):
        self.radius=radius
  
    def CircleArea(self):
        print('area of circle is',3.14*self.radius**2)


class Shape(rectangle,square,Circle):
    def __init__(self, length, breadth,side,radius):
        rectangle.__init__(self,length, breadth)
        square.__init__(self,side)
        Circle.__init__(self,radius)

    def Area_details(self):
        rectangle.rectangleArea(self)
        square.sqaureArea(self)
        Circle.CircleArea(self)


obj=Shape(14,12,14,5)

obj.Area_details()
 