class Student:
    def __init__(self, fullname, marks):
     self.name = fullname
     self.marks = marks
    print("adding new student in DB")
s1 = Student("arjun", "97")
print(s1.name)
print(s1.marks)
s2 = Student("karan", "98")
print(s2.name)
print(s2.marks)
###############################using methods in constructors############
class Bike:
    def __init__(self, model, brand):
        self.model = model
        self .brand = brand

def bike_model(self):
    print("The model of bike is: ")

def bike_brand(self):
    print("The brand of bike is: ")
bike1 = Bike("access125", "Honda")
print(bike1.model)
print(bike1.brand)

