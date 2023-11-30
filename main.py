import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import curses
from menu import menu


def initialize_ui():
    stdscr = curses.initscr()
    stdscr.nodelay(False)  # not blocking cpu goes to 100%
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.timeout(100)
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    return stdscr


def main(stdscr):
    stdscr = initialize_ui()
    menu(stdscr)
    stdscr.refresh()


curses.wrapper(main)
