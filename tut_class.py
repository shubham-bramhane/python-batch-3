# # class Home:
# #     color="blue"


# # object1=Home()
# # print(object1.color)



# # object2=Home()
# # print(object2.color)






# from asyncio.windows_events import NULL
# from ctypes.wintypes import HMODULE


# class home:
#     def __init__(self,color,size,
#     height,width):
#         self.color=color
#         self.size=size
#         self.height=height
#         self.width=width

#     def details(self):
#         print('home details')
#         print('color of house',self.color)
#         print('size of house',self.size)
#         print('height of house',self.height)
#         print('width of house',self.width)






# object2=home('red',100,20,14)

# object2.details()




class rectangle:
    def __init__(self,length,breadth,height):
        self.length=length
        self.breadth=breadth
        self.height=height

    def area(self):
        print('area of rectangle',self.length*self.breadth)


    def volume(self):
        print('volumme of rectangle',self.height*self.breadth*self.length)

    def perimeter(self):
        print('perimeter of rectangle',2*(self.length+self.breadth))




obj1=rectangle(10,12,13)
obj1.area()



obj2=rectangle(50,0,50)
obj2.area()