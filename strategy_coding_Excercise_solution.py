from abc import ABC
import math
import cmath

class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        # will return this part as a complext number
        return complex(b**2 - 4*a*c)


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return float('nan') if (b**2 - 4*a*c) < 0 else complex(b**2 - 4*a*c)


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        D , j = self.strategy.calculate_discriminant(a , b , c) , 1j
        return (
                (-b + cmath.sqrt(D)) / (2 * a) ,
                (-b - cmath.sqrt(D)) / (2 * a)
            )