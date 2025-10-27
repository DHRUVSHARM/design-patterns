# one of the issues in the property observer is demonstrated here where we 
# see that a computed property that depends on another property 
class Event(list):
  def __call__(self, *args, **kwargs):
    for item in self:
      item(*args, **kwargs)


class PropertyObservable:
  def __init__(self):
    self.property_changed = Event()


class Person(PropertyObservable):
  def __init__(self, age=0):
    super().__init__()
    self._age = age

  # derived property 
  @property
  def can_vote(self):
    return self._age >= 18

  # base property 
  @property
  def age(self):
    return self._age

  # @age.setter
  # def age(self, value):
  #   if self._age == value:
  #     return
  #   self._age = value
  #   self.property_changed('age', value)

  @age.setter
  def age(self, value):
    if self._age == value:
      return

    # get the older computed value before changign age, since this depends on age
    old_can_vote = self.can_vote

    # change notify chage of age
    self._age = value
    self.property_changed('age', value)

    # only call can vote if the newer value has changed 
    if old_can_vote != self.can_vote:
      self.property_changed('can_vote', self.can_vote)


if __name__ == '__main__':
  def person_changed(name, value):
    if name == 'can_vote':
      print(f'Voting status changed to {value}')

  p = Person()
  p.property_changed.append(
    person_changed
  )

  for age in range(16, 21):
    print(f'Changing age to {age}')
    p.age = age