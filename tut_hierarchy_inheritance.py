# hierarchy inheritance


# many class combine to form one class 



class sectionA():
    def sectionA_Details(self):
        print('sectionA_Details')



class sectionB():
    def sectionB_Details(self):
        print('sectionB_Details')



class sectionC():
    def sectionC_Details(self):
        print('sectionC_Details')



class section(sectionA,sectionB,sectionC):
    def __init__(self) :
        sectionA().__init__()
        sectionB().__init__()
        sectionC().__init__()

    def section_details(self):
        return sectionA.sectionA_Details(self),sectionB.sectionB_Details(self),sectionC.sectionC_Details(self)
        



obj=section()
obj.section_details()