# this is the child class

from oops_concepts.single_inheritance.Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self,color,mileage,model,year):
        super().__init__(model,year) # to acquire something from parent class
        self.color=color
        self.mileage=mileage

    def display(self): # function overriding , same method is present in parent class(vehicle) - polymorphism
        super().display()
        print(self.color)
        print(self.mileage)

car1=Car("black",2000,"M",2020)
car1.display()