class Demo:
    def __init__(self):
        self.__name = "Demo" #private variable
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name

demo = Demo()
#print(demo.__name)
demo.set_name("Demo")
print(demo.get_name())
