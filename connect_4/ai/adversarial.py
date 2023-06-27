from connect_4.game import Board, Disc
import copy
from random import shuffle


def heuristic(board: Board, color: str):
    if is_connect_4(board, color) or count_connect_3_horizontal_two_adjacent(board, color):
        return 1000
    return (count_connect_3_horizontal_one_adjacent(board, color) +
            count_connect_3_vertical(board, color) +
            count_connect_3_horizontal_one_space(board, color)) * 90 + (
            count_connect_2_vertical(board, color) +
            count_connect_2_horizontal_two_adjacent(board, color)) * 5 + (
            count_connect_2_horizontal_one_adjacent(board, color) * 3)


def is_connect_4(board: Board, color: str) -> bool:
    # Vertical connect
    for slot in board:
        count = 0
        for disc in slot:
            if disc.color == color:
                count += 1
            else:
                count = 0
            if count >= 4:
                return True
    # Horizontal connect
    for i in range(board.max_depth):
        count = 0
        for slot in board:
            if slot[i] is None:
                count = 0
            elif slot[i].color == color:
                count += 1
            else:
                count = 0
            if count >= 4:
                return True
    return False


def count_connect_3_vertical(board: Board, color: str) -> int:
    sum_of_connects = 0
    # Vertical connect
    for slot in board:
        count = 0
        for disc in slot:
            if disc.color == color:
                count += 1
            else:
                count = 0
        if count >= 3 and slot[-1] is None:
            sum_of_connects += 1
    return sum_of_connects


def count_connect_3_horizontal_two_adjacent(board: Board, color: str) -> bool:
    # Horizontal connect. Holes should be like this: _ * * * _
    for i in range(board.max_depth):
        count = 0
        for slot in board:
            # Check if the bottom of empty hole is empty or not
            if i == 0:
                if (slot[i] is None and count == 0) or (slot[i] is None and count == 4) or (
                        slot[i] is not None and slot[i].color == color and count >= 1):
                    count += 1
                else:
                    count = 0
            else:
                if (slot[i - 1] is not None and slot[i] is None and count == 0) or (
                        slot[i - 1] is not None and slot[i] is None and count == 4) or (
                        slot[i] is not None and slot[i].color == color and count >= 1):
                    count += 1
                else:
                    count = 0
            if count == 5:
                return True
    return False


def count_connect_3_horizontal_one_adjacent(board: Board, color: str) -> int:
    sum_of_connects = 0
    # Horizontal connect. Holes should be like this: * * * _ or _ * * *
    for i in range(board.max_depth):
        # * * * _
        count = 0
        for slot in board:
            # Check if the bottom of empty hole is empty or not
            if i == 0:
                if (slot[i] is None and count == 3) or (slot[i] is not None and slot[i].color == color):
                    count += 1
                else:
                    count = 0
            else:
                if (slot[i - 1] is not None and slot[i] is None and count == 3) or (
                        slot[i] is not None and slot[i].color == color):
                    count += 1
                else:
                    count = 0
            if count == 4:
                sum_of_connects += 1
                count = 0
        # _ * * *
        count = 0
        for slot in board:
            # Check if the bottom of empty hole is empty or not
            if i == 0:
                if (slot[i] is None and count == 0) or (slot[i] is not None and slot[i].color == color and count >= 1):
                    count += 1
                else:
                    count = 0
            else:
                if (slot[i - 1] is not None and slot[i] is None and count == 0) or (
                        slot[i] is not None and slot[i].color == color and count >= 1):
                    count += 1
                else:
                    count = 0
            if count == 4:
                sum_of_connects += 1
                count = 0
    return sum_of_connects


def count_connect_3_horizontal_one_space(board: Board, color: str) -> int:
    sum_of_connects = 0
    # Horizontal connect with a space between. Holes should be like this: (* _ * * -) or (- * * _ *)
    for i in range(board.max_depth):
        # * _ * *
        count = 0
        for slot in board:
            # Check if the bottom of empty hole is empty or not
            if i == 0:
                if (slot[i] is None and count == 1) or (
                        slot[i] is not None and slot[i].color == color and (count == 0 or 2 <= count <= 3)):
                    count += 1
                else:
                    count = 0
            else:
                if (slot[i - 1] is not None and slot[i] is None and count == 1) or (
                        slot[i] is not None and slot[i].color == color and (count == 0 or 2 <= count <= 3)):
                    count += 1
                else:
                    count = 0
            if count == 4:
                sum_of_connects += 1
                count = 0
        # * * _ *
        count = 0
        for slot in board:
            # Check if the bottom of empty hole is empty or not
            if i == 0:
                if (slot[i] is None and count == 2) or (
                        slot[i] is not None and slot[i].color == color and (count == 3 or 0 <= count <= 1)):
                    count += 1
                else:
                    count = 0
            else:
                if (slot[i - 1] is not None and slot[i] is None and count == 2) or (
                        slot[i] is not None and slot[i].color == color and (count == 3 or 0 <= count <= 1)):
                    count += 1
                else:
                    count = 0
            if count == 4:
                sum_of_connects += 1
                count = 0
    return sum_of_connects


def count_connect_2_vertical(board: Board, color: str) -> int:
    sum_of_connects = 0
    # Vertical connect
    for slot in board:
        count = 0
        for disc in slot:
            if disc.color == color:
                count += 1
            else:
                count = 0
        if count == 2 and slot[-1] is None:
            sum_of_connects += 1
    return sum_of_connects


def count_connect_2_horizontal_two_adjacent(board: Board, color: str) -> int:
    sum_of_connects = 0
    # Horizontal connect. Holes should be like this: _ * * _ or _ * * _
    for i in range(board.max_depth):
        # _ * * _
        count = 0
        for slot in board:
            # Check if the bottom of empty hole is empty or not
            if i == 0:
                if (slot[i] is None and count == 0) or (slot[i] is None and count == 3) or (
                        slot[i] is not None and slot[i].color == color and count >= 1):
                    count += 1
                else:
                    count = 0
            else:
                if (slot[i - 1] is not None and slot[i] is None and count == 0) or (
                        slot[i - 1] is not None and slot[i] is None and count == 3) or (
                        slot[i] is not None and slot[i].color == color and count >= 1):
                    count += 1
                else:
                    count = 0
            if count == 4:
                sum_of_connects += 1
                count = 0
    return sum_of_connects


def count_connect_2_horizontal_one_adjacent(board: Board, color: str) -> int:
    sum_of_connects = 0
    # Horizontal connect. Holes should be like this: * * _ _ or _ _ * *
    for i in range(board.max_depth):
        # * * _ _
        count = 0
        for slot in board:
            # Check if the bottom of empty hole is empty or not
            if i == 0:
                if (slot[i] is None and 2 <= count <= 3) or (
                        slot[i] is not None and slot[i].color == color and count <= 1):
                    count += 1
                else:
                    count = 0
            else:
                if (slot[i - 1] is not None and slot[i] is None and 2 <= count <= 3) or (
                        slot[i] is not None and slot[i].color == color and count <= 1):
                    count += 1
                else:
                    count = 0
            if count == 4:
                sum_of_connects += 1
                count = 0
        # _ _ * *
        count = 0
        for slot in board:
            # Check if the bottom of empty hole is empty or not
            if i == 0:
                if (slot[i] is None and 0 <= count <= 1) or (
                        slot[i] is not None and slot[i].color == color and count >= 2):
                    count += 1
                else:
                    count = 0
            else:
                if (slot[i - 1] is not None and slot[i] is None and 0 <= count <= 1) or (
                        slot[i] is not None and slot[i].color == color and count >= 2):
                    count += 1
                else:
                    count = 0
            if count == 4:
                sum_of_connects += 1
                count = 0
    return sum_of_connects


# This function generates available actions for a state
def action_space(board: Board) -> list:
    action_space_list = []
    for i, slot in enumerate(board):
        if len(slot) < board.max_depth:
            action_space_list.append(i)
    shuffle(action_space_list)
    return action_space_list


# Applies actions to a state
def successors(board: Board, color: str) -> list:
    new_states = []
    for column in action_space(board):
        board_copy = copy.deepcopy(board)
        i = board_copy[column].fill(Disc(color, column=column))
        board_copy[column][i].row = i
        new_states.append((board_copy, column))
    return new_states


class AlphaBetaPruning:
    def __init__(self, initial_state: Board, max_color: str, min_color: str, cut_off_depth=3):
        self.initial_state = initial_state
        self.cut_off_depth = cut_off_depth
        self.max_color = max_color
        self.min_color = min_color

    def search(self) -> (int, int):
        value, action = self.__max_value(self.initial_state, -1000, 1000, 0)
        return value, action

    def __max_value(self, state, alpha, beta, depth) -> (int, int):
        if depth >= self.cut_off_depth or is_connect_4(state, self.max_color) or is_connect_4(state, self.min_color):
            return heuristic(state, self.max_color) - heuristic(state, self.min_color), None
        best_action = None
        for successor, action in successors(state, self.max_color):
            value, _ = self.__min_value(successor, alpha, beta, depth + 1)
            if value > alpha:
                alpha = value
                best_action = action
            if alpha >= beta:
                # Pruning
                return alpha, best_action
        return alpha, best_action

    def __min_value(self, state, alpha, beta, depth) -> (int, int):
        if depth >= self.cut_off_depth or is_connect_4(state, self.max_color) or is_connect_4(state, self.min_color):
            return heuristic(state, self.max_color) - heuristic(state, self.min_color), None
        best_action = None
        for successor, action in successors(state, self.max_color):
            value, _ = self.__max_value(successor, alpha, beta, depth + 1)
            if value < beta:
                beta = value
                best_action = action
            if alpha >= beta:
                # Pruning
                return beta, best_action
        return beta, best_action
