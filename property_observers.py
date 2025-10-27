# we can use the same events list to 
# listen to property changes 
# again note here that the events here refer to the subscribers
class Event(list):
  def __call__(self, *args, **kwargs):
    for item in self:
      item(*args, **kwargs)

# special class to inherit when we want to observe properties
class PropertyObservable:
  def __init__(self):
    self.property_changed = Event()


class Person(PropertyObservable):
  def __init__(self, name , age=0 , marks=0):
    super().__init__()
    # we will focus on 2 properties
    self._age = age
    self._marks = marks
    self.name = name

  @property
  def age(self):
    return self._age

  # when we are trying to set the age
  # if the value is changed then we call the 
  # property changed events broker 
  @age.setter
  def age(self, value):
    if self._age == value:
      return
    # change the age property 
    self._age = value
    # NOTE : very important point, here when we call the property changed fire call
    # we use reference of the person object itself and call the events, 
    # so any function will have the caller context in it's body by referencing self, 
    # and we do not need to pass it separately as an arg imp :NOTE
    self.property_changed(self ,'age', value)

  
  @property
  def marks(self):
    return self._marks
  
  # here is where we can set when to trigger the changes 
  @marks.setter
  def marks(self, value):
    if self._marks == value:
      return 
    self._marks = value
    self.property_changed(self ,'marks' , value)


# let us say this subscriber cares about 
# marks and age
# we can decide what we care about and also how we care about it
# here what we do is we have only one function which will be 
# able to handle the different property changes
# we can extend this to add multiple people as well
class TrafficAuthority:
  def __init__(self):
    # keep track of current persons observed , we can use a set for this since this is not 
    # going to affect the order of notification and that is managed by the events class 
    self.persons = set()

  def add_people_to_observe(self, person):
    # function to check and add the people to observe
    if person not in self.persons:
      # add to keep track 
      self.persons.add(person)
      # depending on the subscriver which is managed under this traffic authority
      # we can add our custom style on what to when the person changed does
      # this is why this can be called as the context as well
      person.property_changed.append(self.person_changed)

  def person_changed(self, person , name, value):
    # here means we have changed the person in some way
    # how is determined in this implementation using name
    # based on name we can decide what property was actually set (changed while setting to be exact, as that was established 
    # already before in the person class setter of the properties, note that the triggers are fired from there)
    
    # one issue here is we cannot selectively remove listiners on the properties 
    # this can be improved impl' wise 

    # but since we have many persons so we need person

    if name == 'age':
      if value < 16:
        print(f'Sorry, you still cannot drive {person.name}')
      else:
        print(f'Okay, you can drive now {person.name}')
        # while removing can remove from observer list as well
        self.persons.remove(person)
        # we also remnove the observer in this case
        person.property_changed.remove(
          self.person_changed
        )

    elif name == 'marks':
      if value < 33:
        print(f'Sorry, this marks is very very low {person.name}')
      elif 33 <= value <= 100:
        print(f'decent performance, you pass with {value} marks , {person.name}')
      else:
        print(f'Okay, this is crazy !!!!!!! you are tipping off the scales !!!! (you probably lying {person.name})')
        # at this point maybe we decide there is no point of monitoring anymore 
        self.persons.remove(person)
        person.property_changed.remove(
          self.person_changed
        )


if __name__ == '__main__':
  # the way we can think about this is as follows : 
  # 1) traffic authority is something that can be thought of as the subscriber
  # the function we add, is where we can define what to do  
  # here we have 3 persons
  p1 = Person('a')
  p2 = Person('b')
  p3 = Person('c')

  # this single traffic authority will determine the context of the observation and determine actions and monitoring lifecycle 
  ta = TrafficAuthority()

  # now we will add these to make these observable from traffic pov
  ta.add_people_to_observe(p1)
  ta.add_people_to_observe(p2)
  ta.add_people_to_observe(p3)

  # now we check which age triggers observer staements first
  for age in range(14, 20):
    print("\n############################################################################\n")
    print(f'Setting age to {age}')
    p1.age = age
    p2.age = age
    p3.age = age
    print(f"finished setting age to {age}")
    p1.marks = 20
    p2.marks = 80
    p3.marks = 101

    print("\n############################################################################\n")
