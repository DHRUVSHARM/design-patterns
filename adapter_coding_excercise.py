"""
Adapter Coding Exercise
You are given a class called Square and a function calculate_area() 
which calculates the area of a given rectangle.

In order to use Square in calculate_area, 
instead of augmenting it with width/height members, please implement the SquareToRectangleAdapter class.
This adapter takes a square and adapts it in such a way that it can be used as an argument to calculate_area().
"""


from unittest import TestCase


class Square:
    def __init__(self, side=0):
        self.side = side


class Rectangle:
    def __init__(self , width=0 , height=0):
        self.width = width
        self.height = height
    

def calculate_area(rc):
    return rc.width * rc.height


class SquareToRectangleAdapter():

    cache = {}

    def __init__(self, square):
        self.key = hash(square)
        if self.key in self.cache:
            # print("cache hit ...")
            return
        else:
            # print("setting cache ...")
            self.cache[self.key] = square

    @property
    def width(self):
        return self.cache[self.key].side
    
    @property 
    def height(self):
        return self.cache[self.key].side

    

        
        
        

class Evaluate(TestCase):
    def test_exercise(self):
        # adapter is coupled with the square instance
        # can be thought of as a store saving the sq -> rectangle transformation
        # need an adapter instance for each new square
        # class level cache helps memoize some of the work of creation / adaption
        sq = Square(11)
        adapter = SquareToRectangleAdapter(sq)
        self.assertEqual(121, calculate_area(adapter))
        sq.side = 10
        self.assertEqual(100, calculate_area(adapter))

        print("checking caching ...")
        # multiple calls here to the calculation will used the cached version of calculation 
        # from above , as long as the transformations are stored in the adapter memory 
        # HERE YOU WILL SEE CACHING only if we do it by the values not the geometric key, 
        self.assertEqual(200 , 2 * calculate_area(adapter))
        self.assertEqual(300 , 3 * calculate_area(adapter))
        sq.side = 11
        self.assertEqual(1210 , 10 * calculate_area(adapter))
        print("checking caching ...")

                
        print("checking ....")
        # even if the side is the same , since this is a new object and the adapter needs 
        # to track the tranbsformations of the square side and 'adapt' to it, we need it 
        # to have a separate instance , Thus HERE YOU WILL NOT SEE CACHING
        sq2 = Square(10)
        self.assertEqual(100, calculate_area(SquareToRectangleAdapter(sq2)))
        print("checking ....")

        
        sq1 = Square(11)
        self.assertEqual(121 , calculate_area(SquareToRectangleAdapter(sq1)))

