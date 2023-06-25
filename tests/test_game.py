import unittest
from connect_4.game import Game, HumanAgent


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.player1 = HumanAgent('p1', 'red')
        self.player2 = HumanAgent('p2', 'yellow')
        self.game = Game(self.player1, self.player2)
    
    def test_board1(self):
        for slot in self.game.board:
            self.assertEqual(len(slot), 0)
        self.game.drop_disc(1)
        self.assertEqual(1, len(self.game.board[1]))
        self.game.drop_disc(1)
        self.assertEqual(2, len(self.game.board[1]))
        self.assertEqual('red', self.game.board[1][0].color)
        self.assertEqual('yellow', self.game.board[1][1].color)

    def test_board2(self):
        self.game.drop_disc([1] * 6)
        self.assertRaises(IndexError, self.game.drop_disc, 1)

    def test_win_vertical1(self):
        for i in range(6):
            self.game.drop_disc(i % 2)
            self.assertIsNone(self.game.win())
        self.game.drop_disc(0)
        self.assertEqual(self.player1, self.game.win())

    def test_win_vertical2(self):
        self.game.drop_disc([0, 0] + [0, 2] * 3)
        self.game.drop_disc(0)
        self.assertEqual(self.player1, self.game.win())

    def test_win_horizontal(self):
        self.game.drop_disc([0, 1, 2, 0, 3, 1, 4, 0, 5])
        self.assertEqual(self.player1, self.game.win())


if __name__ == '__main__':
    unittest.main()
