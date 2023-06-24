from connect_4 import player


class Disc:
    def __init__(self, color: str, row=None, column=None):
        self.color = color
        self.row = row
        self.column = column


class Board:
    def __init__(self, max_slots: int, max_depth: int):
        self.max_slots = max_slots
        self.max_depth = max_depth
        self.slots = [Slot(max_depth) for _ in range(max_slots)]

    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        i = self.index
        if i >= self.max_slots:
            raise StopIteration
        self.index += 1
        return self.slots[i]
    
    def __getitem__(self, item):
        return self.slots[item]
    
    def __len__(self):
        return self.max_slots


class Slot:
    def __init__(self, max_depth: int):
        self.max_depth = max_depth
        self.holes = [None for _ in range(max_depth)]

    def __len__(self):
        return len(list(filter(lambda x: x is not None, self.holes)))

    def __getitem__(self, item):
        return self.holes[item]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        i = self.index
        if i >= self.__len__():
            raise StopIteration
        self.index += 1
        return self.holes[i]

    def fill(self, disc: Disc) -> int:
        if self.__len__() == self.max_depth:
            raise IndexError('The slot is full!')
        i = self.holes.index(None)
        self.holes[i] = disc
        return i


class Game:
    def __init__(self, player1: player.HumanAgent, player2=None, slots=7, depth=6):
        self.board = Board(slots, depth)
        if player2 is None:
            player2 = player.AIAgent()
        player1.board = self.board
        player2.board = self.board
        self.players = (player1, player2)
        self.turn = 0

    # TODO: Overload this method
    def drop_disc(self, slot: int) -> (Disc, bool):
        disc = self.players[self.turn].drop_disc(slot)
        self.turn = ~self.turn
        # TODO: Check the win logic
        return disc, self.win_logic()

    def win_logic(self):
        # Vertical
        for i in self.board.slots:
            if len(i) < 4:
                continue
            color = i[0].color
            count = 1
            for disc in i:
                if color == disc.color:
                    count += 1
                else:
                    color = disc.color
                    count = 1
                if count >= 4:
                    return True
        # Horizontal
        for i in range(self.board.max_depth):
            color = None
            count = 0
            for j in range(1, self.board.max_slots):
                if self.board.slots[j][i] is None:
                    count = 0
                    color = None
                elif color == self.board.slots[j][i].color:
                    count += 1
                else:
                    color = self.board.slots[j][i].color
                    count = 1
                if count >= 4:
                    return True
        return False
