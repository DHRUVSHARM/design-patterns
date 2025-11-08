from abc import ABC

# inherting from this will give acesss to print 
# using method resolution order (MRO).
# reflective since the structure of the class object is inspected 
# at runtime and decisions are made accordingly
# here stil adding new expressions would need the expression printer to be modified 
class Expression(ABC):
    pass


class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.right = right
        self.left = left


class ExpressionPrinter:
    @staticmethod
    def print(e, buffer):
        """ Will fail silently on a missing case. """
        if isinstance(e, DoubleExpression):
            buffer.append(str(e.value))
        elif isinstance(e, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print(e.left, buffer)
            buffer.append('+')
            ExpressionPrinter.print(e.right, buffer)
            buffer.append(')')

    # monkey patch at runtime, when the class definition is run
    # top to bottom, then this is executed (before we reach the __main__ block)
    # or before import if this class was imported 
    Expression.print = lambda self, b: ExpressionPrinter.print(self, b)


# still breaks OCP because new types require M×N modifications

if __name__ == '__main__':
    # represents 1+(2+3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    buffer = []

    # ExpressionPrinter.print(e, buffer)

    # IDE might complain here
    e.print(buffer)

    print(''.join(buffer))
