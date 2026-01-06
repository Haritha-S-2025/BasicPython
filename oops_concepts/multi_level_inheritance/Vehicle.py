
# this is the parent class, model and year are the attributes

class Vehicle:
    def __init__(self,model,year):
        self.model=model
        self.year=year

    def display(self):
        print("The model is : ",self.model)
        print("In the year : ",self.year)

