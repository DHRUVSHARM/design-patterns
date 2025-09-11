import random

class Database:
    initialized = False

    # will run after new despite which object was returned
    def __init__(self):
        self.id = random.randint(1,101)
        print('Generated an id of ', self.id)
        print('Loading database from file')
        

    _instance = None
    # allocates memory
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls)\
                .__new__(cls, *args, **kwargs)

        return cls._instance


database = Database()

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    # last set of properties will be picked up since you can note that the instance created is the same 

    print(d1.id, d2.id)
    #  both will point to the last generated id in in the init
    # cpython based id on address
    print(id(d1) , id(d2))
    # unique memory address id is same
    print(d1 == d2)
    print(database == d1)
    print(database == d2)