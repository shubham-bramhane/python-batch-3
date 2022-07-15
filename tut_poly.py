class poco:
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color

    def result_details(self):
        print('name->',self.name)
        print('price->',self.price)
        print('color->',self.color)


class nokia:
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color

    def result_details(self):
        print('name->',self.name)
        print('price->',self.price)
        print('color->',self.color)


obj=poco('pc1',14000,'black')
obj2=nokia('c1',10000,"blue")





for data in (obj,obj2):
    data.result_details()






