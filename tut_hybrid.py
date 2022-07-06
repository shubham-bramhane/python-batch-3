

class Main():
    def Main_details(self):
        print('main details')





class subA(Main):
    def subA_details(self):
        print('sub a details')



class subB(Main):
    def subB_details(self):
        print('sub b details')



class Combine(subA,subB):
    pass




obj=Combine()
obj.subB_details()