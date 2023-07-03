import unittest
from connect_4.game import Game, HumanAgent
from connect_4.ai.adversarial import count_connect_3_vertical, count_connect_3_horizontal_two_adjacent, \
    count_connect_3_horizontal_one_adjacent, action_space, successors


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

    def test_count_connect_3_vertical(self):
        self.game.drop_disc([0, 1, 0, 1, 0, 1, 4, 4, 4, 5, 4, 5, 4, 4])
        self.assertEqual(1, count_connect_3_vertical(self.game.board, self.player1.color))
        self.assertEqual(1, count_connect_3_vertical(self.game.board, self.player2.color))

    def test_count_connect_3_horizontal_two_adjacent(self):
        self.game.drop_disc([0, 1, 3, 1, 4, 1, 5, 0, 3, 0, 4, 3, 5, 4])
        self.assertEqual(1, count_connect_3_horizontal_two_adjacent(self.game.board, self.player1.color))

    def test_count_connect_3_horizontal_one_adjacent1(self):
        self.game.drop_disc([0, 3, 1, 3, 4, 4, 6, 6, 5])
        self.assertEqual(0, count_connect_3_horizontal_one_adjacent(self.game.board, self.player1.color))

    def test_count_connect_3_horizontal_one_adjacent2(self):
        self.game.drop_disc([0, 1, 3, 1, 4, 1, 5, 0, 3, 0, 4, 3, 5, 4, 5, 6])
        self.assertEqual(2, count_connect_3_horizontal_one_adjacent(self.game.board, self.player1.color))
        self.game.drop_disc([4, 2, 3, 2])
        self.assertEqual(1, count_connect_3_horizontal_one_adjacent(self.game.board, self.player1.color))

    def test_action_space(self):
        self.game.drop_disc([1] * 6)
        self.game.drop_disc([3] * 6)
        self.assertListEqual([0, 2, 4, 5, 6], action_space(self.game.board, shuffle=False))

    def test_successors(self):
        self.game.drop_disc([1] * 6)
        self.game.drop_disc([3] * 6)
        successors_list = successors(self.game.board, self.player1.color, shuffle=False)
        self.assertEqual(2, successors_list[1][1])
        self.assertEqual(5, len(successors_list))
        # Check the deep copy
        self.assertIsNone(self.game.board[0][0])
        self.assertIsNotNone(successors_list[0][0][0][0])
        self.assertIsNone(successors_list[1][0][0][0])


if __name__ == '__main__':
    unittest.main()
