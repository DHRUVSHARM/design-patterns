# here this will be used as the list of the subscribers to the mediator
# we will store them here
# each entry will represent the specific persons subscriver copy and list of actions they perform when 
# the events are fired we can also handle how they respond to events in general 
class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

# this can be thought of as a mediator, which in this case will simply take the args and fire off all subscribers
class Game:
    def __init__(self):
        print("initialized the event list ..") 
        self.events = Event()

    # all functions are fired with the specific args
    # how to handle the args is upto you and based on the function passed
    # the args can be thought of as the info pertaining to the event
    # so think of it as something that happens in a game
    def fire(self, args):
        self.events(args)


# we try to store information pertaining to the event here 
# event : goal was scored
class GoalScoredInfo:
    def __init__(self, who_scored, goals_scored):
        self.goals_scored = goals_scored
        self.who_scored = who_scored

# event injury 
class Injury:
    def __init__(self , injured_player , injury_count):
        self.player_injured = injured_player
        self.injury_count = injury_count


# these can be thought of as the subscribers that use the game mediator 
# these will define the interfaces to expose to the outside world and will trigger updates across the broker 
class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.goals_scored = 0
        self.injury_count = 0
        self.is_injury = False

    def score(self):
        self.goals_scored += 1
        # updated event which we will use to fire all the listeners
        args = GoalScoredInfo(self.name, self.goals_scored)
        self.game.fire(args)
    
    def injured(self):
        self.is_injury = True
        self.injury_count += 1
        args = Injury(self.name , self.injury_count)
        # use mediator and fire 
        self.game.fire(args)


# these are the subscribers that will subscribe to the events that happen in the game 
# key point to note here is that we use the game mediator to subscirbe, which uses the event broker 
# what all actions we want to subscribe to, and what we want to do as a result of each of the events we listen to is decided by us
# on instantiation here for example we want to add to functions to respond to scoring goals as well as to injuries
# also notes that this is dynamic so when someone joins , and then an event of interest happens, 
# then obviously at that point the state of the game is what will be seen (from that point on)
# similarly if someone is removed then the updates will no longer go to them so
# that is the advantage of the event broker usage as the underlying method for the mediator here 


# will be there since the start of the game 
class Coach:
    def __init__(self, game):
        game.events.append(self.celebrate_goal)
        game.events.append(self.appeal_on_injury)

    # celebrates first 2 goals 
    def celebrate_goal(self, args):
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            print(f'Coach says: well done, {args.who_scored}!')

    # coach appeals on second injury 
    def appeal_on_injury(self, args):
        if isinstance(args , Injury) and args.injury_count > 1:
            print(f"Coach appeals : my player is injured {args.injury_count} times !!!!!")


# will join after the goals and the 3rd injury to drive home my point
# we can also have some information that will help
# for example we can 
class Parent:
    def __init__(self, children, game):
        self.children = children
        game.events.append(self.celebrate_goal)
        game.events.append(self.concern_on_injury)

    # respond to goals from child
    def celebrate_goal(self, args):
        if isinstance(args , GoalScoredInfo) and args.who_scored in self.children:
            print(f"Parent celebrates : my child {args.who_scored} has scored !!!")
    
    # respond to injuries from child
    def concern_on_injury(self, args):
        if isinstance(args , Injury) and args.player_injured in self.children:
            print(f"Parent concerns : my child is injured !!!!")
    


# will be there since the start of the game 
class HealthWorker:
    def __init__(self , game):
        game.events.append(self.respond_to_injury)
    

    def respond_to_injury(self, args):
        if isinstance(args , Injury):
            print(f"Healthcare response for {args.player_injured}")



if __name__ == '__main__':
    game = Game()
    
    # 2 players, coach, healthcare worker at start
    sam = Player('Sam', game)
    john = Player('John' , game)
    coach = Coach(game)
    worker = HealthWorker(game)


    sam.score()  # Coach says: well done, Sam!
    sam.injured() # health worker response no appeal by coach
    sam.score()  # Coach says: well done, Sam!
    sam.injured() # coach appeal, healthcare response
    sam.score()  # ignored by coach

    # john's parent joins 
    john_parent = Parent(['John'] , game)

    john.score() # coach and parent responds
    sam.score() # no response
    sam.injured() # coach appeal , worker appeal parent not care

    john.injured() # parent respond , healthcare worker
    john.score() # coach parent
    john.score() # parent only
