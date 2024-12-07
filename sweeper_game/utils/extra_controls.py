from sweeper_game.sweeper import Sweeper_game

def zero_clear(row, col, env):
    if env.get_tile(int(row)-1, int(col)) == -3:
        env.step(Sweeper_game.ACTION.CHECK, int(row)-1, int(col))
        if env.get_tile(int(row)-1, int(col)) == 0:
            zero_clear(int(row)-1, int(col), env=env)
    if env.get_tile(int(row)+1, int(col)) == -3:
        env.step(Sweeper_game.ACTION.CHECK, int(row)+1, int(col))
        if env.get_tile(int(row)+1, int(col)) == 0:
            zero_clear(int(row)+1, int(col), env=env)
    if env.get_tile(int(row), int(col)-1) == -3:
        env.step(Sweeper_game.ACTION.CHECK, int(row), int(col)-1)
        if env.get_tile(int(row), int(col)-1) == 0:
            zero_clear(int(row), int(col)-1, env=env)
    if env.get_tile(int(row), int(col)+1) == -3:
        env.step(Sweeper_game.ACTION.CHECK, int(row), int(col)+1)
        if env.get_tile(int(row), int(col)+1) == 0:
            zero_clear(int(row), int(col)+1, env=env)
    if env.get_tile(int(row)-1, int(col)-1) == -3:
        env.step(Sweeper_game.ACTION.CHECK, int(row)-1, int(col)-1)
        if env.get_tile(int(row)-1, int(col)-1) == 0:
            zero_clear(int(row)-1, int(col)-1, env=env)
    if env.get_tile(int(row)-1, int(col)+1) == -3:
        env.step(Sweeper_game.ACTION.CHECK, int(row)-1, int(col)+1)
        if env.get_tile(int(row)-1, int(col)+1) == 0:
            zero_clear(int(row)-1, int(col)+1, env=env)
    if env.get_tile(int(row)+1, int(col)-1) == -3:
        env.step(Sweeper_game.ACTION.CHECK, int(row)+1, int(col)-1)
        if env.get_tile(int(row)+1, int(col)-1) == 0:
            zero_clear(int(row)+1, int(col)-1, env=env)
    if env.get_tile(int(row)+1, int(col)+1) == -3:
        env.step(Sweeper_game.ACTION.CHECK, int(row)+1, int(col)+1)
        if env.get_tile(int(row)+1, int(col)+1) == 0:
            zero_clear(int(row)+1, int(col)+1, env=env)