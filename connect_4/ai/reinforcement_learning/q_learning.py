from connect_4.game import Board, Game, AIAgent
from connect_4.ai.adversarial import action_space
from . import q_table


class QLearningAgent(AIAgent):
    def __init__(self, color: str):
        super().__init__(color)
        self.state_action_stack = []

    def drop_disc(self, slot: int):
        state = simplify_board(self.board, self.color)
        action = pick_best_action(self.board, state)
        self.state_action_stack.append((state.board, action, state.color_number))
        return super().drop_disc(action)

    def win(self) -> None:
        calculate_new_q_value(1000, self.state_action_stack)

    def lose(self) -> None:
        calculate_new_q_value(-1000, self.state_action_stack)

    def draw(self) -> None:
        calculate_new_q_value(0, self.state_action_stack)


class State:
    def __init__(self, board: list, color_number: int):
        self.board = board
        self.color_number = color_number

    def __repr__(self):
        return str(self.board)


def simplify_board(board: Board, color: str) -> State:
    simple = list(map(list, board))
    zero_color = None
    for slot in simple:
        for j, disc in enumerate(slot):
            if zero_color is None or zero_color == disc.color:
                zero_color = disc.color
                slot[j] = 0
            else:
                slot[j] = 1
    color_number = 0 if zero_color is None or color == zero_color else 1
    return State(simple, color_number)


def pick_best_action(board: Board, state: State) -> int:
    max_q = q_table[(q_table['state'].apply(lambda x: x == state)) & (q_table['color'] == state.color_number)].sort_values(by='quality', ascending=False)
    if len(max_q) == 0:
        return action_space(board)[0]
    if max_q.at[0, 'quality'] >= 0:
        return max_q.at[0, 'action']
    actions = action_space(board)
    if len(actions) == len(max_q):
        return max_q.at[0, 'action']
    return list(filter(lambda x: len(max_q[max_q['action'] == x]) == 0, actions))[0]


def calculate_new_q_value(reward: int, sas: list) -> None:
    discount_factor = 0.5
    learn_factor = 0.5
    future_q = 0  # TODO: calculate future_q
    for i in range(len(sas) - 1, -1, -1):
        state, action, color = sas[i]
        old_q = q_table[(q_table['state'].apply(lambda x: x == state)) & (q_table['action'] == action) & (q_table['color'] == color)]
        old_q = old_q.at[0, 'quality'] if (exist := len(old_q) > 0) else 0
        new_q = (1 - learn_factor) * old_q + learn_factor * (reward + discount_factor * future_q)
        if exist:
            q_table.loc[(q_table['state'].apply(lambda x: x == state)) & (q_table['action'] == action) & (
                        q_table['color'] == color), 'quality'] = new_q
        else:
            q_table.loc[len(q_table.index)] = [state, action, color, new_q]
        future_q = new_q
        reward = 0


def train(count_games: int):
    for _ in range(count_games):
        agent1 = QLearningAgent('0')
        agent2 = QLearningAgent('1')
        game = Game(agent1, agent2)
        while game.win() is None and not game.draw():
            game.drop_disc(-1)

        if game.draw():
            agent1.draw()
            agent2.draw()
        elif game.win() == agent1:
            agent1.win()
            agent2.lose()
        else:
            agent1.lose()
            agent2.win()
    q_table.to_csv('q_table.csv', index=False)
