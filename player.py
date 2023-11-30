def print_user_life(stdscr, life):
    height, _ = stdscr.getmaxyx()
    stdscr.addstr(height // 2 - 6, 1, "HP")

    for i in range(height // 2 - 5, (height // 2 - 5) + 10):
        if i < (height // 2 - 5) + (life // 10):
            stdscr.addstr(i, 1, "██")
        else:
            stdscr.addstr(i, 1, "░░")
