# imp points to note here :
# start point root adds all the steps as we call the function , then one command to apply all stuff in the chain once built
# in sequence

class Creature:
    # basic class with attack and defense values 
    # this can be thought of as the base state on which we will apply the modifiers
    def __init__(self, name, attack, defense):
        self.defense = defense
        self.attack = attack
        self.name = name


    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'

# this class is key, and can be though of as the class that manages the chain of responsibility
class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        # will store the link to the next modifier in the chain 
        self.next_modifier = None

    # recursive of sorts, we keep calling till no next modifer 
    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    # the handle function is called after each step does it's indiviual work to move further the chain
    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()
    # optional terminate
    def terminate(self):
        print("terminating due to invalid conditons !!!!! , not going further down the chain ...")


class NoBonusesModifier(CreatureModifier):
    def handle(self):
        print('No bonuses for you!')
        super().handle()


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f'Doubling {self.creature.name}''s attack')
        self.creature.attack *= 2
        super().handle()

# conditional modifier
class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f'Increasing {self.creature.name}''s defense')
            self.creature.defense += 1
        elif self.creature.attack >= 8:
            # terminate chain on invalid condition
            super().terminate()
            # optionally we can also call terminate 
        else:
            super().handle()


if __name__ == '__main__':
    goblin = Creature('Goblin', 1, 1)
    print("initially : " , goblin)

    root = CreatureModifier(goblin)

    # another way to have termination is to simply take a special no bonuses class and make it not call handle
    root.add_modifier(NoBonusesModifier(goblin))

    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))

    # no effect but still goes to next modifier
    root.add_modifier(IncreaseDefenseModifier(goblin))
    root.add_modifier(NoBonusesModifier(goblin))

    # increasing one more time will terminate and not go to next step
    root.add_modifier(DoubleAttackModifier(goblin))
    # terminate defined here 
    root.add_modifier(IncreaseDefenseModifier(goblin))
    root.add_modifier(NoBonusesModifier(goblin))

    root.handle()  # apply modifiers
    print("finally : " , goblin)
