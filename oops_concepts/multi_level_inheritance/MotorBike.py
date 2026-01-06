from oops_concepts.multi_level_inheritance.Bike import Bike


class MotorBike(Bike):
    def __init__(self,brand,model,year,color):
        super().__init__(brand,model,year)
        self.color=color

    def display(self):
        super().display()
        print(self.color)

motorbike1=MotorBike("BM",1,2025,"blue")
motorbike1.display()

