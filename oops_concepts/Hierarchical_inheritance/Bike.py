from oops_concepts.Hierarchical_inheritance.Vehicle import Vehicle


class Bike(Vehicle):
    def vehicle_details(self):
        super().vehicle_details()
        print("Two wheeler")

bike=Bike()
bike.vehicle_details()
