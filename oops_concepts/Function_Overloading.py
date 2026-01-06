class Greet:
    def greeting(self,name=None):#default function / function with default values
        if name:
            print("Hello ",name)
        else:
            print("Hello")

greet = Greet()
greet.greeting("HARITHA")#name=None aayath kond enth parameter venamengilum kodukkam
greet.greeting()