# # # without using encapsulation

# # # class rectangle():
# # #     def __init__(self,length):
# # #         self.length=length

# # #     def details(self):
# # #         print('length->',self.length)


# # # obj=rectangle(10)
# # # obj.details()
# # # print(obj.length)


# # # there are two method for encapsulation 



# # # 1) protected mode 
# # # 2) private mode




# # # private virable can not be access outside the class and in base class it can only access in parent class

# # # the variable can be private using "__" double underscore



# # # class parent():
# # #     def __init__(self):
# # #         self.__a="python"

# # #     def details(self):
# # #         print('details ->',self.__a)


# # # class child(parent):
# # #     def __init__(self):
# # #         super().__init__()





# # # # obj=parent()
# # # # obj.details()
# # # # print(obj.__a)



# # # obj=child()
# # # obj.details()
# # # print(obj.__a)



# # #protected mode




# # # protected mode -> the class variable cannot be accessed outside the class but can be access within the class and base class

# # # a variable can be protected using "_"  single undescore 






# # class parent():
# #     def __init__(self):
# #         self._a='python'

# #     def details(self):
# #         print('detials->',self._a)




# # # obj=parent()
# # # obj.details()
# # # print(obj._a)


# # class child(parent):
# #     def __init__(self):
# #         super().__init__()


# # obj=child()
# # obj.details()
# # print(obj._a)




# # class rectangle():
# #     def __init__(self,length,breadth):
# #         self.__length=length
# #         self.breadth=breadth

# #     def area(self):
# #         print('area is ->',self.__length*self.breadth)



# # class subclass(rectangle):
# #     def __init__(self, length, breadth):
# #         super().__init__(length, breadth)


# # obj=rectangle(15,16)
# # obj.area()
# # print(obj.__length)


# # obj=subclass(15,14)
# # obj.area()
# # print(obj.breadth)
# # print(obj.__length)



# class user():
#     def __init__(self,name,password):
#         self.__name=name
#         self.__password=password 
    
#     def detials(self):
#         print('name->',self.__name)
#         print('password',self.__password)

# obj=user("shubham",'0987654321')

# # obj.detials()
# print(obj.__name)
# print(obj.__password)





class parent():
    def __init__(self):
        self._a='python'

    def detials(self):
        print('detials->',self._a)


class child(parent):

    def __init__(self):
        super().__init__()

        print('before modifing ->',self._a)

        self._a='python2'


        print('after modifing ->',self._a)


obj=child()
obj1=parent()
print(obj._a)
print(obj1._a)