from oops_concepts.Hierarchical_inheritance.Vehicle import Vehicle


class Car(Vehicle):
    def vehicle_details(self):
        print("Car is a 4 wheeler")

car=Car()
car.vehicle_details()
car.vehicle_features()