# here the event class can be thought of as a set of subscriber functions that are attached
# observer design using events to observe events
# bigger idea is that the single person object instance can add observers to the actions happeing as part of the obsrvable class
# here person object is used to add observer functions that can be notified when certain actions happen as part of the person class itself
# in a way an object of person class can respond to different actions in the class
class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

        # these can be thought of as event subscriber refs
        self.falls_ill = Event()
        self.dentist_call = Event()

    # actions determine who to notify ( which set to notify )
    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)

    def develop_a_toothache(self):
        self.falls_ill(self.name , self.address)
        self.dentist_call(self.name , self.address)
        # can add more series of events if needed

def call_doctor(name, address):
    print(f'A doctor has been called to {address}')

def call_dentist(name , address):
    print(f'A dentist has been called to {address}')


if __name__ == '__main__':
    person = Person('Sherlock', '221B Baker St')

    # add 2 subscribers when falling ill
    person.falls_ill.append(lambda name, addr: print(f'{name} is ill'))
    person.falls_ill.append(call_doctor)

    # add one subscriber to the dentist call
    person.dentist_call.append(call_dentist)

    # invoke subscriber calls on catching a cold
    person.catch_a_cold()

    # and you can remove subscriptions too
    person.falls_ill.remove(call_doctor)

    # will only invoke the lambda function 
    person.catch_a_cold()

    # dentist call + whatever subscriber left to be ill
    person.develop_a_toothache()