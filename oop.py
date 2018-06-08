class Person:

    def __init__(self):
        self.name = ""
        self.age = ""

        #self.__name = "I am private"
        #self._nickname = "I am protected"
        #self.streetName = "I am public"


    def __del__(self):
        print("The garbage collector came for: ", self.name)

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age


bob = Person()
bob.setName("Bob")
bob.setAge(45)
print(bob.name)

peter = Person()
peter.setName("Peter")
print(peter.name)
