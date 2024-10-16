######### practice questions
class Circle:
    def __init__(self, r):
        self.r = r
    def area_circle(self):
        area = (3.14 * (self.r * self.r))
        return area
    def perimeter(self):
        peri = (2 * 3.14 * self.r)
        return peri
c1 = Circle(5)
print(c1.area_circle())
print(c1.perimeter())
############practice question 2
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    def show_details(self):
       print( "role=", self.role)
       print("department=", self.department)
       print("salary=", self.salary)


class Engineer(Employee):
    def __add__(self, name, age):
        self.name = name
        self. age = age
        super().__init__("Developer", "IT", 65000)

eng1 = Engineer("Developer", "IT", 65000,)
eng1.show_details()

#####################
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def __gt__(self, order2):
          return self.price > order2.price
odr1 = Order("chips", "30")
odr2 = Order("coffee", "20")
print(odr1 > odr2)


