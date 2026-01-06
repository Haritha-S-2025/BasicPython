

from oops_concepts.hybrid_inheritance.Animal import Animal
#from oops_concepts.hybrid_inheritance.Cat import Cat
from oops_concepts.hybrid_inheritance.Cat1 import Cat1


class Kitten(Animal,Cat1):
    def kitten_sound(self):
        super().cat_sound()
        print("kitten sound")

kitten = Kitten()
kitten.kitten_sound()
#kitten.cat_sound()
#kitten.make_sound()