from connect_4.ai.adversarial import action_space
from connect_4.game import Board, Game, AIAgent
from . import q_table


def simplify_board(board: Board) -> (list, str | None):
    simple = list(map(list, board))
    zero_color = None
    for slot in simple:
        for j, disc in enumerate(slot):
            if zero_color is None or zero_color == disc.color:
                zero_color = disc.color
                slot[j] = 0
            else:
                slot[j] = 1
    return simple, zero_color


def pick_best_action(board: Board, turn: int) -> int:
    state = simplify_board(board)
    max_q = q_table[(q_table['state'] == state) & (q_table['disc'] == turn)].sort_values(by='quality', ascending=False)
    if len(max_q) == 0:
        return action_space(board)[0]
    if max_q.at[0, 'quality'] >= 0:
        return max_q.at[0, 'action']
    actions = action_space(board)
    if len(actions) == len(max_q):
        return max_q.at[0, 'action']
    return list(filter(lambda x: len(max_q[max_q['action'] == x]) == 0, actions))[0]


def calculate_new_q_value(reward: int, sas: list) -> None:
    future_q = 0
    for i in range(len(sas) - 1, -1, -1):
        state, action, disc = sas[i]
        old_q = q_table[(q_table['state'].apply(lambda x: x == state)) & (q_table['action'] == action) & (q_table['disc'] == disc)]
        if len(old_q) > 0:
            old_q = old_q.at[0, 'quality']
        else:
            old_q = 0
            q_table.loc[len(q_table.index)] = [state, action, disc, old_q]

        new_q = (1 - learn_factor) * old_q + learn_factor * (reward + discount_factor * future_q)
        q_table.loc[(q_table['state'].apply(lambda x: x == state)) & (q_table['action'] == action) & (q_table['disc'] == disc), 'quality'] = new_q
        future_q = new_q


def train(count_games: int):
    for _ in range(count_games):
        agent1 = AIAgent('0')
        agent2 = AIAgent('1')
        game = Game(agent1, agent2)
        while True:
            simplified_board, zero = simplify_board(game.board)
            zero = agent1.color if zero is None else zero
            one_color = agent1.color if agent2.color == zero else agent2.color
            map_color = {zero: 0, one_color: 1}
            disc_color = map_color[game.players[game.turn].color]
            action = pick_best_action(game.board, disc_color)
            state_action_stack[game.turn].append((simplified_board, action, disc_color))
            game.drop_disc(action)
            winner = game.win()
            if winner is None:
                continue
            if game.draw():
                calculate_new_q_value(0, state_action_stack[0])
                calculate_new_q_value(0, state_action_stack[1])
            elif winner == agent1:
                calculate_new_q_value(1000, state_action_stack[0])
                calculate_new_q_value(-1000, state_action_stack[1])
            else:
                calculate_new_q_value(-1000, state_action_stack[0])
                calculate_new_q_value(1000, state_action_stack[1])
            break
    q_table.to_csv('q_table.csv')


state_action_stack = [[], []]
discount_factor = 0.5
learn_factor = 0.5
