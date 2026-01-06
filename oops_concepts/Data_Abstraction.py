from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod #annotation
    def sound(self):
        pass

    def eat(self):
        print("Animal eats")

#create another class
class Cat(Animal):
    def sound(self):
        print("Cat makes meow")

cat= Cat()
cat.sound()
cat.eat()