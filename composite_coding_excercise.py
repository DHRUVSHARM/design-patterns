"""
Composite Coding Exercise
Consider the code presented below. We have two classes called SingleValue and ManyValues. 
SingleValue stores just one numeric value, 
but ManyValues can store either numeric values or SingleValue objects.

You are asked to give both SingleValue and ManyValues 
a property member called sum that returns a sum of 
all the values that the object contains. 
Please ensure that there is only a single method that realizes the property sum, not multiple methods.

Here is a sample unit test:

class FirstTestSuite(unittest.TestCase):
    def test(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)
"""


from collections.abc import Iterable
import unittest
from abc import ABC, abstractmethod



class Summable(Iterable , ABC ):

    def _sum(self):
        result = 0
        for element in self:
            if element == self:
                return element.value
            else:
                result += element.sum

        return result

    @abstractmethod
    def __iter__(self):
        pass


class SingleValue(Summable):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}"
    
    def __iter__(self):
        yield self

    @property
    def sum(self):
        return super()._sum()



class ManyValues(list , Summable):
    def __init__(self):
        super().__init__()
        # to create a composition of objects
        self.children = []

    def append(self, object):
        # also add to children for the composition
        self.children.append(object)
        super().append(object)

    def __str__(self):
        # for now this can just take the list superclass
        return super().__str__()
    
    def __iter__(self):
        for element in self.children:
            if isinstance(element , int):
                yield SingleValue(element)
            else:
                yield element

    @property
    def sum(self):
        return super()._sum()

class FirstTestSuite(unittest.TestCase):
    def test(self):
        single_value = SingleValue(11)
        
        self.assertEqual(single_value.sum , 11)
        print(single_value)

        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)

        self.assertEqual(other_values.sum , 55)
        print(other_values)        

        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        self.assertEqual(all_values.sum , 11)

        all_values.append(other_values)
        
        self.assertEqual(all_values.sum, 66)