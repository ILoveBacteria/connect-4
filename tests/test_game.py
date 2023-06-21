import unittest
from connect_4.game import Game, HumanAgent


class MyTestCase(unittest.TestCase):
    def test_board1(self):
        game = Game(HumanAgent('p1', 'red'), HumanAgent('p2', 'yellow'))
        for s in game.board.slots:
            self.assertEqual(len(s), 0)
        game.drop_disc(1)
        self.assertEqual(1, len(game.board.slots[1]))
        game.drop_disc(1)
        self.assertEqual(2, len(game.board.slots[1]))
        self.assertEqual('red', game.board.slots[1].holes[0].color)
        self.assertEqual('yellow', game.board.slots[1].holes[1].color)

    def test_board2(self):
        game = Game(HumanAgent('p1', 'red'), HumanAgent('p2', 'yellow'), depth=3)
        game.drop_disc(1)
        game.drop_disc(1)
        game.drop_disc(1)
        self.assertRaises(IndexError, game.drop_disc, 1)


if __name__ == '__main__':
    unittest.main()
