

class rectangle():
    def __init__(self,length):
        self.length=length

    def rectangle_details(self):
        print('length->',self.length)


class subclass(rectangle):
    def __init__(self, length,breadth):
        rectangle.__init__(self,length)
        self.breadth=breadth

    def subclass_details(self):
        print('length->',self.length)
        print('breadth->',self.breadth)



class subclass2(rectangle):
    def __init__(self,height):
        
        self.height=height

    def subclass2_details(self):
        print('length->',self.length)
        print('height ->',self.height)


class combine(subclass,subclass2):
    def __init__(self, length, breadth,height):
        subclass.__init__(self,length, breadth)
        subclass2.__init__(self,height)

    def combine_details(self):
        print('length->',self.length)
        print('breadth->',self.breadth)
        print('height->',self.height)

obj=combine(14,12,13)

obj.combine_details()


# name
# dob
# address


