
class Rectangle():
    def __init__(self,length):
        self.length=length

    def Rectangle(self):
        print('length is ->',self.length)


class subRectangle(Rectangle):
    def __init__(self, length,breadth):
        Rectangle.__init__(self,length)
        self.breadth=breadth

    def subrectangle(self):
        print('length is ->',self.length)
        print('breadth is ->',self.breadth)



class sub2Rectangle(Rectangle):
    def __init__(self,height):
        
        
        self.height=height

    def sub2Rectangle(self):
        print('length is ->',self.length)
        print('height is->',self.height)


class Combine(subRectangle,sub2Rectangle):
    def __init__(self, length, breadth,height):
        subRectangle.__init__(self,length,breadth)
        sub2Rectangle.__init__(self,height)
    
    def Combine(self):
        print('length is ->',self.length)
        print('breadth is ->',self.breadth)
        print('height is ->',self.height)
       
obj=Combine(14,12,15)
obj.sub2Rectangle()






