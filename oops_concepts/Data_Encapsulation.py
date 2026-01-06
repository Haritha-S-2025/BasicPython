class Person:
    def __init__(self,name,age,password):
        self.name = name #public visibility mode, it can be accessed by any other packages(same or outside the package)
        self._age = age #protected(_) , protected variables
        self.__password = password #private(__) , visible only within the class , can be accessed by getter and setter methods,

    #data encapsulation : get_password and set_password
    def get_password(self):# for data retrieval
        return self.__password

    def set_password(self,password):#for data updation
        self.__password = password

person1=Person("Hritha",24,"Haritha123")
print(person1.name)
print(person1._age)
