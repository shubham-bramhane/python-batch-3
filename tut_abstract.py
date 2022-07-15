from abc import ABC,abstractmethod






# # class Parent(ABC):
# #     @abstractmethod
# #     def data(self):
# #         pass

# # class child(Parent):
# #     def result(self):
# #         print('this is child class')


# #     def data(self):
# #         pass


# # obj=child()
# # obj.result()




# class mobile(ABC):
#     def game(self):
#         print('i am playing game ')

#     def video(self):
#         print('i m watching video')

#     @abstractmethod
#     def camera(self):
#         pass




# class child(mobile):
#     def camera(self):
#         print('i am capturing a photo')


# # obj=child()
# # obj.camera()



# obj=mobile()
# obj.camera()





class rectangle(ABC):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    @abstractmethod
    def area(self):
        pass



class child(rectangle):
    def area(self):
        print('area of rectangle',self.length*self.breadth)






# obj=rectangle(14,12)
# obj.details()        



obj=child(14,15)
obj.area()