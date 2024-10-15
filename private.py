##should be used inside of the class not accessible outside the class##
class Acc:
    def __hello(self):
        print("hello person!")
    def welcome(self):
        self.__hello()


a1 = Acc()
print(a1.welcome())


