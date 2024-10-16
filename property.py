class Student:
      def __init__(self, phy, math, eng):
          self.phy = phy
          self.math = math
          self.eng = eng
      @property
      def cal_percentage(self):
          return str((self.phy+self.math+self.eng)/3)+"%"
s1 = Student(97, 98, 99)
print(s1.cal_percentage)
s1.phy =79
print(s1.cal_percentage)