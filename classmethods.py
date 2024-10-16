class Person:
    name = "anonymous"
    def changename(self, name):
        self.name = name
p1 = Person()
p1.changename("anil")
print(p1.name)
print(Person.name)
#########to change the class attributes we use class methods

class Person:
    name = "anonymous"
    @classmethod
    def changename(cls, name):
        cls.name = name
p1 = Person()
p1.changename("anil")
print(p1.name)
print(Person.name)


