import pygame
import os
from level1 import level1

script_dir = os.path.dirname(__file__)

pygame.init()
pygame.mixer.init()
music = pygame.mixer.Sound("audio/menu_song.mp3")
music.play(loops=-1)


def menu(stdscr):
    height, width = stdscr.getmaxyx()
    is_first_time = True

    while True:
        stdscr.refresh()
        stdscr.addstr(height // 2 - 4, width // 2 - 11, "┏┳┓   ┓          ┓    ")
        stdscr.addstr(height // 2 - 3, width // 2 - 11, " ┃ ┏┓┏┣┓┏┓┏┓┏┓┏┓┏┫┏┓┏┓")
        stdscr.addstr(height // 2 - 2, width // 2 - 11, " ┻ ┗ ┗┛┗┛┗┗┛┣┛┗┻┗┻┛ ┗ ")
        stdscr.addstr(height // 2 - 1, width // 2 - 11, "            ┛         ")
        stdscr.addstr(height // 2 + 1, width // 2 - 8, "[0] QUIT [1] PLAY")

        if not pygame.mixer.get_busy():
            music.play(loops=-1)

        key_pressed = stdscr.getch()

        if 32 <= key_pressed <= 126:
            if chr(key_pressed) == "0":
                exit()
            if chr(key_pressed) == "1":
                stdscr.clear()
                music.stop()
                level1(stdscr, is_first_time)
                is_first_time = False

