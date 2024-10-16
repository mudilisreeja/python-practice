class Car:
    def __init__(self, car_type):
        self.car_type = car_type
    @staticmethod
    def satrt():
        print("car is started")
    @staticmethod
    def stop():
        print("car is stopped")
class Toyotocar(Car):
    def __init__(self, brand, car_type):
        self.brand = brand
        super().__init__(car_type)

car1 = Toyotocar("prius", "electric")
print(car1.brand)
print(car1.car_type)








