from oops_concepts.multiple_inheritance.Father import Father
from oops_concepts.multiple_inheritance.Mother import Mother


class Child(Father, Mother):
    def skills(self):
        super().skills()
        print("child enjoy")

child1 = Child()
child1.skills()


#Here the child class calls Super().skills, it will invoke the first parent class, here it invokes the skills of the parent class
