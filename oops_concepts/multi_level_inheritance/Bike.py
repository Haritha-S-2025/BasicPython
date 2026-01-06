from oops_concepts.multi_level_inheritance.Vehicle import Vehicle


class Bike(Vehicle):
    def __init__(self,brand,model,year):
        super().__init__(brand,model)
        self.brand=brand
    def display(self):
        super().display()
        print(self.brand)