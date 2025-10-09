import random
import string
import sys

class User:
    def __init__(self, name):
        self.name = name

# using flyweight
class User2:
    # used to store the unique strings will be 200 in our example 
    # once the strings are added, their indexes do not change , hence used ordered structure like list here 
    strings = []
 
    def __init__(self, full_name):
        def get_or_add(s):
            # simple function the idea here is to return the index if name present else add it and return index
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings)-1
        # at the user 2 object level this will act like a lookup of sorts to map the index -> correct string stored in the static 
        # variable
        self.names = [get_or_add(x) for x in full_name.split(' ')]

    def __str__(self):
        return ' '.join([self.strings[x] for x in self.names])  

def random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for x in range(8)])


if __name__ == '__main__':
    users = []

    first_names = [random_string() for x in range(100)]
    last_names = [random_string() for x in range(100)]

    # storing 100 * 100 as separate user objects is redundant 
    # we can build a pointer to a common store instead 
    for first in first_names:
        for last in last_names:
            users.append(User(f'{first} {last}'))

    # newer class
    u2 = User2('Jim Jones')
    u3 = User2('Frank Jones')
    print(u2.names)
    print(u3.names)
    print(User2.strings)

    users2 = []
    

    # each of the user2 object references underlying strings effectively reducing memory to o(first_names + last_names)
    for first in first_names:
        for last in last_names:
            users2.append(User2(f'{first} {last}'))

    print(users2[-1])