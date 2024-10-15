#########single inheritance########
class Car:
    @staticmethod
    def start():
        print("car is started")
    @staticmethod
    def stop():
        print("car is stopped")

class Toyotocar(Car):
     def __init__(self, type):
         self.type = type
car1 = Toyotocar("ELECTRIC")
print(car1.type)
car1.start()
car1.stop()
#######multi level inheritance###########
