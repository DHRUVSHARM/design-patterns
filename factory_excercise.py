"""
Factory Coding Exercise
You are given a class called Person . The person has two attributes: id , and name .

Please implement a  PersonFactory that has a non-static  create_person()  method that takes a person's name and return a person initialized with this name and an id.

The id of the person should be set as a 0-based index of the object created. So, the first person the factory makes should have Id=0, second Id=1 and so on.

"""

from itertools import count


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    # class level config , will be independent of the objects , factory dependent 
    auto_initialized_id = count(0)

    """
    def __init__(self , factory_id = 0):
        # object level config , depends on the factory instance
        self.factory_id = factory_id
    """

    def create_person(self , name):
        # returns the current value and moves to the next
        person_id = next(self.auto_initialized_id)
        return Person(person_id , name)


p1 = PersonFactory(1)
p2 = PersonFactory(2)

p1.create_person("Dhruv")
p1.create_person("Dhruv")


p2.create_person("Dhruv")
p2.create_person("Dhruv")


p1.create_person("Dhruv")

