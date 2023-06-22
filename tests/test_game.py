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

    def test_win_vertical1(self):
        game = Game(HumanAgent('p1', 'red'), HumanAgent('p2', 'yellow'))
        for i in range(6):
            self.assertFalse(game.drop_disc(i % 2))
        self.assertTrue(game.drop_disc(0))

    def test_win_vertical2(self):
        game = Game(HumanAgent('p1', 'red'), HumanAgent('p2', 'yellow'), depth=10)
        self.assertFalse(game.drop_disc(0))  # winner
        self.assertFalse(game.drop_disc(1))
        self.assertFalse(game.drop_disc(0))
        self.assertFalse(game.drop_disc(0))
        for i in range(5):
            self.assertFalse(game.drop_disc(i % 2))
        self.assertFalse(game.drop_disc(2))
        self.assertTrue(game.drop_disc(0))

    def test_win_horizontal(self):
        game = Game(HumanAgent('p1', 'red'), HumanAgent('p2', 'yellow'))
        self.assertFalse(game.drop_disc(0))  # winner
        self.assertFalse(game.drop_disc(1))
        self.assertFalse(game.drop_disc(2))  # winner
        for i in range(3, 5):
            self.assertFalse(game.drop_disc(i % 3))
            self.assertFalse(game.drop_disc(i))  # winner
        self.assertFalse(game.drop_disc(0))
        self.assertTrue(game.drop_disc(5))


if __name__ == '__main__':
    unittest.main()
