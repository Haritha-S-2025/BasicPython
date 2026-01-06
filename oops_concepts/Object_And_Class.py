
#class name always starts with capital letter
#self ; keyword : to refer the current object attributes
#__init__ : is used to create a constructor ; used to initialize an object
# class variable : change cheyyatha values class variable aayitt kodukkam
#in the output the class variables is same for every objects


class Student:
    school_name="ABC" #class variable/ global variable ; it is invoked by using the class name
    def __init__(self,name,age): #name,age are the attributes
        print("this is a constructor")
        self.name=name #instance variables
        self.age=age #instance variables

    def display(self):
        print("Name is :",self.name)
        print("Age is :",self.age)
        print("School is :",Student.school_name) # Global variable is invoked here

#object creation
student1=Student("Haritha",25)
student1.display()
student2=Student("Ammu",23)
student2.display()
