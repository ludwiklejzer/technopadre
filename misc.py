import curses


def type(stdscr, dialog):
    stdscr.timeout(50)
    height, width = stdscr.getmaxyx()
    skip = False

    for text in dialog:
        stdscr.clear()
        for index, char in enumerate(text):
            stdscr.addstr(height // 2 - 1, (width // 2 - len(text) // 2) + index, char)
            stdscr.refresh()
            key = stdscr.getch()
            if stdscr.getch() == curses.KEY_ENTER or key == 10:
                skip = True
                break

        if skip == False:
            action_message = "Pressione ENTER para continuar"
            while stdscr.getch() != ord("\n"):
                stdscr.addstr(
                    height - 3, width // 2 - len(action_message) // 2, action_message
                )
        else:
            skip = False
            continue

        stdscr.clear()

    stdscr.timeout(100)
