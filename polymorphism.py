class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def show_num(self):
        print (self.real, "i+ ", self.img,"j ")
        ######Dunder function
    def __add__(self, num1):
        new_real = num1.real + self.real
        new_img = num1.img + self.img
        return complex(new_real, new_img)

c1 = Complex(3, 5)
c1.show_num()
num1 = Complex(4, 6)
num1.show_num()
num2 =c1.__add__(num1)
print(num2)


