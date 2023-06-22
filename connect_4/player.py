from abc import abstractmethod, ABC
from connect_4 import game


class Player(ABC):
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        self.board = None

    @abstractmethod
    def drop_disc(self, slot: int) -> (int, int):
        pass


class AIAgent(Player):
    def __init__(self):
        super(AIAgent, self).__init__('AI', 'Blue')

    def drop_disc(self, slot) -> (int, int):
        pass


class HumanAgent(Player):
    def __init__(self, name: str, color: str):
        super(HumanAgent, self).__init__(name, color)

    def drop_disc(self, slot) -> (int, int):
        y = self.board.slots[slot].fill(game.Disc(self.color))
        return slot, y
