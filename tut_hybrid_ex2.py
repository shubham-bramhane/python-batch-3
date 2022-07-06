




class University:
  def __init__(self,univ):
    self.univ = univ
  def display(self):  # Method to print the University Name:
    print(f"The University name is: {self.univ}")

# 1st Derived or Child Class of University Class:
class Course(University):
  def __init__(self,univ,course):
    # using "super" keyword to access members of the parent class having same name:
    print("Constructor of the Child Class 1 of Class University")
    University.__init__(self,univ)
    self.course = course
  def display(self):  # Method to print the Course Name:
    # using "super" keyword to access display method defined in the parent class:
    print(f"The Course name is: {self.course}")
    University.display(self)

# 2nd Derived or Child Class of University Class:
class Branch(University):
  def __init__(self,branch):
    print("Constructor of the Child Class 2 of Class University")
    self.branch = branch
  def display(self):  # Method to print the Branch Name:
    print(f"The Branch name is: {self.branch}")

# Derived or Child Class of Class Course and Branch:
class Student(Course, Branch):
  def __init__(self,univ,course,branch):
    print("Constructor of Child class of Course and Branch is called")
    self.name = "Tonny"
    Branch.__init__(self,branch)
    Course.__init__(self,univ,course)
  def display(self):
    print(f"The Name of the student is: {self.name}")
    Branch.display(self)
    Course.display(self)

# Object Instantiation:
ob = Student('mit','computer','cs')  # Object named ob of the class Student.
print()
ob.display()    # Calling the display method of Student class.


