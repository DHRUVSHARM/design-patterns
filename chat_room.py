# in this mediator example the chatroom selected will be the mediator between differen people in the same room 
# persons can join or leave the room , but the chatroom itself does not have references to the persons at all times
# it is in fact the reverse, ie; 
# person1 -----> room
# person2 -----> same room
# ans so on..

# the person class holds reference to the chatroom 
# it also defines the implementation to the outside world 
# internally it calls the functions of the room
class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room = None

    # chatroom driven update
    def receive(self, sender, message):
        # this is the updater of sorts . this function is used to interact with the updates from 
        # the room and record it for the person itself for biderectional communication 
        s = f'{sender}: {message}'
        print(f'[{self.name}\'s chat session] {s}')
        self.chat_log.append(s)


    # person driven actions
    def say(self, message):
        # a public message
        self.room.broadcast(self.name, message)

    def private_message(self, who, message):
        # a private message 
        self.room.message(self.name, who, message)


# we have all the people stored as lookup 
# even the update functions are written in a stateless manner
# this class is concerned mostly with the implementation of how communication and
# members are managed within the room
class ChatRoom:
    def __init__(self):
        self.people = []

    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)


    # person joins the room
    def join(self, person):
        join_msg = f'{person.name} joins the chat'
        # send broadcast to all in the room , so the 'room' is kind of like a dummy element
        self.broadcast('room', join_msg)
        person.room = self
        self.people.append(person)


    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)
    
    # person leaves the room 
    def leave(self , person):
        leave_msg = f'{person.name} left the chat'
        # remove the person first , give them a message 
        self.message('room' , person.name , 'you have been kicked out ..')
        self.people.remove(person)
        person.room = None
        # send a broadcast to everyone , it will not reach the person removed 
        self.broadcast('room' , leave_msg)



if __name__ == '__main__':
    room = ChatRoom()

    john = Person('John')
    jane = Person('Jane')

    # no one to listen to broadcast
    room.join(john)
    
    # john gets notified
    room.join(jane)

    # simple chat
    john.say('hi room')
    jane.say('oh, hey john')

    # john and jane get notified
    simon = Person('Simon')
    room.join(simon)

    # broadcast to all 
    simon.say('hi everyone!')
    
    # dm to simon from jane
    jane.private_message('Simon', 'glad you could join us!')
    
    # dm back 
    simon.private_message('Jane' , 'thanks for asking  !!!!!')

    print("\n****************************\n")
    # simon removed from the room (can also do it at the person level)
    # private kick out message to simon 
    # and public broadcast to the remainder that that simon has left
    room.leave(simon)