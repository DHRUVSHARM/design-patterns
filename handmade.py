from enum import Enum, auto

# states can be thought of as nodes
class State(Enum):
    OFF_HOOK = auto()
    CONNECTING = auto()
    CONNECTED = auto()
    ON_HOLD = auto()
    ON_HOOK = auto()


# triggers can be used as edge descriptions determining the action
# think of it as what you would write on the edge
class Trigger(Enum):
    CALL_DIALED = auto()
    HUNG_UP = auto()
    CALL_CONNECTED = auto()
    PLACED_ON_HOLD = auto()
    TAKEN_OFF_HOLD = auto()
    LEFT_MESSAGE = auto()


if __name__ == '__main__':

    # the modelling for this can be in the form of a dfa, nfa
    rules = {
        State.OFF_HOOK: [
            (Trigger.CALL_DIALED, State.CONNECTING)
        ],
        State.CONNECTING: [
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.CALL_CONNECTED, State.CONNECTED)
        ],
        State.CONNECTED: [
            (Trigger.LEFT_MESSAGE, State.ON_HOOK),
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.PLACED_ON_HOLD, State.ON_HOLD)
        ],
        State.ON_HOLD: [
            (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
            (Trigger.HUNG_UP, State.ON_HOOK)
        ]
    }
    
    # in this case we will terminate when we reach the exit state
    state = State.OFF_HOOK
    exit_state = State.ON_HOOK

    while state != exit_state:
        # we display current state
        print(f'The phone is currently {state}')

        # list the triggers
        for i in range(len(rules[state])):
            t = rules[state][i][0]
            print(f'{i}: {t}')

        # select trigger with index
        idx = int(input('Select a trigger:'))
        
        # new state is got by picking the second value
        s = rules[state][idx][1]
        state = s

    print('We are done using the phone.')