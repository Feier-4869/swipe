from math import sqrt
class Triangle(object):

     def __init__(self, a, b, c):
         self._a = a
         self._b = b
         self._c = c

     @staticmethod
     def is_valid(a, b, c):
         return True if a + b > c and a + c > b and b + c > a else False

     def perimeter(self):
         return self._a + self._b + self._c

     def area(self):
         return self._a * self._b * self._c


if __name__ == '__main__':
    if Triangle.is_valid(7, 7, 5):
        tri = Triangle(7, 7, 5)
        print(tri._a)
        print(tri.perimeter())
    else:
        print('无法构成三角形')
