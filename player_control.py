from sweeper_game.sweeper import Sweeper_game
from sweeper_game.utils.extra_controls import zero_clear

env = Sweeper_game()

rows, cols, num_mines = map(int, input().split())
env.render(rows, cols, num_mines)

status = True
while status:
    env.print_board()
    action, row, col = input().split()
    if action == 'check':
        status = env.step(Sweeper_game.ACTION.CHECK, int(row), int(col))
        if env.get_tile(int(row), int(col)) == 0:
            zero_clear(int(row), int(col), env=env)
    elif action == 'flag':
        status = env.step(Sweeper_game.ACTION.FLAG, int(row), int(col))
    elif action == 'unflag':
        status = env.step(Sweeper_game.ACTION.UNFLAG, int(row), int(col))