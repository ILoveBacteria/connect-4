from connect_4.game import Board, Disc
import math
import copy


def heuristic(board: Board, max_color: str):
    if is_connect_4(board, max_color) or count_connect_3_horizontal_two_adjacent(board, max_color):
        return math.inf
    return (count_connect_3_horizontal_one_adjacent(board, max_color) + count_connect_3_vertical(board, max_color)) * 9


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
                if (slot[i] is None and count == 0) or \
                        (slot[i] is None and count == 4) or \
                            (slot[i].color == color and count >= 1):
                    count += 1
                else:
                    count = 0
            else:
                if (slot[i - 1] is not None and slot[i] is None and count == 0) or \
                        (slot[i - 1] is not None and slot[i] is None and count == 4) or \
                            (slot[i].color == color and count >= 1):
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
        count = 0
        # * * * _
        for slot in board:
            # Check if the bottom of empty hole is empty or not
            if i == 0:
                if (slot[i] is None and count == 3) or (slot[i].color == color):
                    count += 1
                else:
                    count = 0
            else:
                if (slot[i - 1] is not None slot[i] is None and count == 3) or (slot[i].color == color):
                    count += 1
                else:
                    count = 0
            if count == 4:
                sum_of_connects += 1
                count = 0
        # _ * * *
        for slot in board:
            # Check if the bottom of empty hole is empty or not
            if i == 0:
                if (slot[i] is None and count == 0) or (slot[i].color == color and count >= 1):
                    count += 1
                else:
                    count = 0
            else:
                if (slot[i - 1] is not None and slot[i] is None and count == 0) or (slot[i].color == color and count >= 1):
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
    def __init__(self, initial_state: Board, max_color: str, cut_off_depth=3):
        self.initial_state = initial_state
        self.cut_off_depth = cut_off_depth
        self.max_color = max_color

    def search(self) -> (int, int):
        value, action = self.__max_value(self.initial_state, -1 * math.inf, math.inf, 0)
        return value, action

    def __max_value(self, state, alpha, beta, depth) -> (int, int):
        if depth >= self.cut_off_depth:
            return heuristic(state, self.max_color), None
        best_action = None
        for successor, action in successors(state):
            value, _ = self.__min_value(successor, alpha, beta, depth + 1)
            if value > alpha:
                alpha = value
                best_action = action
            if alpha >= beta:
                # Pruning
                return alpha, best_action
        return alpha, best_action

    def __min_value(self, state, alpha, beta, depth) -> (int, int):
        if depth >= self.cut_off_depth:
            return heuristic(state), None
        best_action = None
        for successor, action in successors(state):
            value, _ = self.__max_value(successor, alpha, beta, depth + 1)
            if value < beta:
                beta = value
                best_action = action
            if alpha >= beta:
                # Pruning
                return beta, best_action
        return beta, best_action
