# this is an example of the intrusive visitor 
# here we need to change the implementation of print / eval in both the 
# classes if we want to evaluate or aggregate the expression , hence the word 'INTRUSIVE'
# this becomes a problem if the class hierarchy is very large
# too many classes 
class DoubleExpression:
    def __init__(self, value):
        self.value = value

    def print(self, buffer):
        buffer.append(str(self.value))

    def eval(self): return self.value


class AdditionExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left

    def print(self, buffer):
        buffer.append('(')
        self.left.print(buffer)
        buffer.append('+')
        self.right.print(buffer)
        buffer.append(')')

    def eval(self):
        return self.left.eval() + self.right.eval()


if __name__ == '__main__':
    # represents 1+(2+3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    # we can think of this buffer as the visitor in this case 
    buffer = []
    e.print(buffer)
    print(''.join(buffer), '=', e.eval())

    # breaks OCP: requires we modify the entire hierarchy
    # what is more likely: new type or new operation? 
    # new type means we want another kind of expression, this is possible
    # since there is a tendency to reuse the base objects (types) in more unique ways
    # new ways will cause change in hierarchy structures and the visitor would have to be modified / added 
    # accordingly, for each class causing issues, types can be fixed after a certain point and it is easy to think about the 
    # the repr for the basic types, but how the different types interact can cause different kinds of problems if 
    # we try and manage that intrusively within each class
