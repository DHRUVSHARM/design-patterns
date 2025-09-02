from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    # redeclaration won't work
    # def __init__(self, rho, theta):

    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * sin(b)
            self.y = a * cos(b)

        # steps to add a new system
        # 1. augment CoordinateSystem
        # 2. change init method

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))

    # inner class style, more sense in a language like java
    class Factory:

        def __init__(self , bias = 1):
            self.bias = bias
        
        def new_cartesian_point(self , x, y):
            return Point(self.bias * x, self.bias * y)

    # factory = Factory()

# take out factory methods to a separate class
class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))


if __name__ == '__main__':
    # p1 = Point(2, 3, CoordinateSystem.CARTESIAN)
    # p2 = PointFactory.new_cartesian_point(1, 2)
    # or you can expose factory through the type
    p3_factory = Point.Factory(bias = 100)
    p3 = p3_factory.new_cartesian_point(5, 6)
    print(p3)

    p3_factory = Point.Factory(bias = 200)
    p3 = p3_factory.new_cartesian_point(5, 6)
    print(p3)

    p3_factory = Point.Factory()
    p3 = p3_factory.new_cartesian_point(5, 6)
    print(p3)
    # p4 = Point.factory.new_cartesian_point(7, 8)
    # print(p1, p2, p3, p4)
