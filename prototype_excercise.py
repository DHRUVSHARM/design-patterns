"""
Prototype Coding Exercise
Given the definitions shown in code, you are asked to implement Line.deep_copy()  
to perform a deep copy of the given Line  object. 
This method should return a copy of a Line that contains copies of its start/end points.

Note: please do not confuse deep_copy() with __deepcopy__()!
"""

from copy import deepcopy
from enum import Enum

class PrototypeEnum(Enum):
    SIMPLE = "simple_line_prototype"
    CURVED = "curved_line_prototype"
    DASHED = "dashed_line_prototype"


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class LineFactory:

    simple_line_prototype = None
    curved_line_prototype = None
    dashed_line_prototype = None

    @classmethod
    def __create_prototype(cls , proto , proto_name):
        # for now for all line types, the prototype is the same
        if proto is None: 
            if proto_name == PrototypeEnum.SIMPLE:
                cls.simple_line_prototype = Line(Point(0 , 0) , Point(0 , 0))
                return cls.simple_line_prototype
            elif proto_name == PrototypeEnum.CURVED:
                cls.curved_line_prototype = CurvedLine(Point(0 , 0) , Point(0 , 0) , 0)
                return cls.curved_line_prototype
            elif proto_name == PrototypeEnum.DASHED:
                cls.dashed_line_prototype = DashedLine(Point(0 , 0) , Point(0 , 0) , 0)
                return cls.dashed_line_prototype
            else:
                # simple handling for now
                raise LookupError
        return proto


    @staticmethod
    def __new_line(proto , start , end , proto_name=PrototypeEnum.SIMPLE):
        derived_proto = LineFactory.__create_prototype(proto , proto_name)
        result = deepcopy(derived_proto)
        result.start.x = start.x
        result.start.y = start.y
        result.end.x = end.x
        result.end.y = end.y
        return result


    @staticmethod
    def new_simple_line(start , end):
        return LineFactory.__new_line(LineFactory.simple_line_prototype , start , end)

    @staticmethod
    def new_curved_line(start , end , slope):
        # add a slope 
        clp = LineFactory.__new_line(LineFactory.curved_line_prototype , start , end , PrototypeEnum.CURVED)
        clp.slope = slope
        return clp

    @staticmethod
    def new_dashed_line(start , end , dash_intensity):
        # add a dash intensity
        dlp = LineFactory.__new_line(LineFactory.dashed_line_prototype , start , end , PrototypeEnum.DASHED)
        dlp.dash_intensity = dash_intensity
        return dlp

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        # in this case we will make a simple copy using the simple line and return it 
        return LineFactory.new_simple_line(self.start , self.end)
    
class CurvedLine:
    def __init__(self, start=Point(), end=Point() , slope=0):
        self.start = start
        self.end = end
        self.slope = slope

    def deep_copy(self): 
        return LineFactory.new_curved_line(self.start , self.end , self.slope)
    
class DashedLine:
    def __init__(self, start=Point(), end=Point(), dash_intensity=0):
        self.start = start
        self.end = end
        self.dash_intensity = dash_intensity

    def deep_copy(self): 
        return LineFactory.new_dashed_line(self.start , self.end , self.dash_intensity)



if __name__ == "__main__":
    # Test simple line
    l1 = Line(Point(1, 1), Point(2, 2))
    l2 = l1.deep_copy()
    print("Simple Line Original:", l1.start.x, l1.start.y, l1.end.x, l1.end.y)
    print("Simple Line Copy    :", l2.start.x, l2.start.y, l2.end.x, l2.end.y)
    print("Different objects?  ", l1 is not l2, "Different points?", l1.start is not l2.start)

    print("-" * 50)

    # Test curved line
    c1 = CurvedLine(Point(0, 0), Point(3, 3), slope=5)
    c2 = c1.deep_copy()
    print("Curved Line Original:", c1.start.x, c1.start.y, c1.end.x, c1.end.y, "slope:", c1.slope)
    print("Curved Line Copy    :", c2.start.x, c2.start.y, c2.end.x, c2.end.y, "slope:", c2.slope)
    print("Different objects?  ", c1 is not c2, "Different points?", c1.start is not c2.start)

    print("-" * 50)

    # Test dashed line
    d1 = DashedLine(Point(0, 0), Point(4, 4), dash_intensity=10)
    d2 = d1.deep_copy()
    print("Dashed Line Original:", d1.start.x, d1.start.y, d1.end.x, d1.end.y, "dash:", d1.dash_intensity)
    print("Dashed Line Copy    :", d2.start.x, d2.start.y, d2.end.x, d2.end.y, "dash:", d2.dash_intensity)
    print("Different objects?  ", d1 is not d2, "Different points?", d1.start is not d2.start)

