from math import sqrt

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def move_to(self, x, y):
        self.x = x
        self. y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance(self, other):
        print(other, type(other))
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)

    def __str__(self):
        return '(%s, %s)' %(str(self.x), str(self.y))

    # def __str__(self):
if __name__ == '__main__':
    p1 = Point(1, 3)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(5, 6)
    print(p2)
    print(p1.distance(p2))