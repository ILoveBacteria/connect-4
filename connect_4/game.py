from .player import AIAgent, HumanAgent


class Disc:
    def __init__(self, color: str):
        self.color = color


class Board:
    def __init__(self, max_slots: int, max_depth: int):
        self.max_slots = max_slots
        self.max_depth = max_depth
        self.slots = [Slot(max_depth) for _ in range(max_slots)]


class Slot:
    def __init__(self, max_depth: int):
        self.max_depth = max_depth
        self.holes = [None for _ in range(max_depth)]

    def __len__(self):
        return len(list(filter(lambda x: x is not None, self.holes)))

    def fill(self, disc: Disc) -> int:
        if self.__len__() == self.max_depth:
            raise ValueError('The slot is full!')
        i = self.holes.index(None)
        self.holes[i] = disc
        return i


class Game:
    def __init__(self, player1: HumanAgent, player2=None, slots=7, depth=6):
        self.board = Board(slots, depth)
        if player2 is None:
            player2 = AIAgent()
        player1.board = self.board
        player2.board = self.board
        self.players = (player1, player2)
        self.turn = 0

    def drop_disc(self, slot: int):
        pass
