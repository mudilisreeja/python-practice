class car:
    @staticmethod
    def start():
        print("car is started")
    @staticmethod
    def stop():
        print("car is stopped")

class Toyotocar(car):
       def __init__(self, type):
           self.type = type
class Fortunecar(Toyotocar):
       def __init__(self, color):
        self.color = color


car1 = Fortunecar("electric")
car1 = Fortunecar("blue")
print(car1.color)
print(car1.type)
car1.start()
car1.stop()


