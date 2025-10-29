# interesting but not practical :)
from abc import ABC


class Switch:
    def __init__(self):
        # starting with the off state 
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


# abstract base class state 
# you can think of this as the default state, hence if something is 
# on or off already it means we can print already on / off
# think of this like the default handler for invalid states, 
# when something like off -> off, the off implemnentation bubbles up to here
class State(ABC):
    def on(self, switch):
        print('Light is already on')

    def off(self, switch):
        print('Light is already off')

# this is the on state, the only place it can go is off
class OnState(State):
    def __init__(self):
        print('Light turned on')

    def off(self, switch):
        # override the default off, to show that we are coming from on -> off
        print('Turning light off...')
        switch.state = OffState()


class OffState(State):
    def __init__(self):
        print('Light turned off')

    def on(self, switch):
        print('Turning light on...')
        switch.state = OnState()


if __name__ == '__main__':
    sw = Switch()

    sw.on()  # Turning light on...
             # Light turned on

    sw.off()  # Turning light off...
              # Light turned off

    sw.off()  # Light is already off


