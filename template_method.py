from abc import ABC


# high level algo described here 
class Game(ABC):

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        # store index of the current player
        self.current_player = 0

    # skeleton
    def run(self):
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f'Player {self.winning_player} wins!')

    def start(self): pass

    @property
    def have_winner(self): pass

    def take_turn(self): pass

    @property
    def winning_player(self): pass

# implementation is through inheritance
class Chess(Game):
    def __init__(self):
        super().__init__(2)
        self.max_turns = 10
        self.turn = 1

    def start(self):
        print(f'Starting a game of chess with {self.number_of_players} players.')

    @property
    def have_winner(self):
        return self.turn == self.max_turns

    def take_turn(self):
        print(f'Turn {self.turn} taken by player {self.current_player}')
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def winning_player(self):
        return self.current_player


if __name__ == '__main__':
    chess = Chess()
    # run is like the tempalte method
    chess.run()