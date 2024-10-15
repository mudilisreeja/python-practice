####Hiding implementation details of class and showing the essential features to users
class Car:
    def __init__(self):
      self.acc = False
      self.brk = False
      self.clutch = False
    def start(self):
     self.acc = True
     self.clutch = True
    print("car started")


car1 = Car()
car1.start()