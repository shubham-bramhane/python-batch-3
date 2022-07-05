# from calendar import c


# a-> b

# a->b -> c

# a-b 
# a-c



# multiple inheritance  their is one parent and many child class that inherit the property from base class 


# class Main():
#     def main_details(self):
#         print('this is main class')

    

# class subClass1(Main):
#     def subClass1_details(self):
#         print('subclass 1')
        


# class subClass2(Main):
#     def subClass2_details(self):
#         print('subclass 2')
        


# class subClass3(Main):
#     def subClass3_details(self):
#         print('subclass 3')
    


# obj=subClass1()
# obj.main_details()




class rectangle():
    def __init__(self,length):
        self.length=length

    def length_details(self):
        print('length is -> ',self.length)



class area(rectangle):
    def __init__(self, length,breadth):
        super().__init__(length)
        self.breadth=breadth

    def area_details(self):
        print('length- >',self.length)
        print('breadth- >',self.breadth)
        






class volume(rectangle):
    def __init__(self, length,height):
        super().__init__(length)
        self.height=height

    def volume_details(self):
        print('length- >',self.length)
        print('height- >',self.height)
        


obj=volume(14,20)
obj.volume_details()