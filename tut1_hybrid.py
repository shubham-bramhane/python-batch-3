# hybrid inheritance is the mixture of 2 or more types of inehritance


class main():
    def main_details(self):
        print('main class')


class subclass1(main):
    def subclass1_details(self):
        print('sub class 1 detaills')
        



class subclass2(main):
    def subclass2_details(self):
        print('sub class 2 details')
        



class combine(subclass1,subclass2):
    def combine(self):
        subclass1.subclass1_details(self)
        subclass2.subclass2_details(self)


obj=combine()
obj.combine()