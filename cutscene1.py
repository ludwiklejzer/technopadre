import curses
import pygame
import time
import os
from misc import type

script_dir = os.path.dirname(__file__)


def cutscene1(stdscr, is_first_time):
    # key_pressed = stdscr.getch()
    height, width = stdscr.getmaxyx()

    if is_first_time:
        cutscene_music = pygame.mixer.Sound("./audio/cutscene_music.mp3")
        cutscene_music.play(loops=-1)

        stdscr.addstr(height - 3, width // 2 - 8, "Brasil - Ano 1998")

        pygame.mixer.init()
        pygame.mixer.music.load(script_dir + "/audio/telephone_dial_and_call.mp3")
        pygame.mixer.music.play()

        stdscr.refresh()

        while pygame.mixer.music.get_busy():
            stdscr.addstr(height - 3, width // 2 - 8, "                 ")
            continue

        dialog = [
            "[Cliente]: Alô! É da Demotech?",
            "[Demotech]: Sim. Em que podemos ajudar?",
            "[Cliente]: Preciso de ajuda urgente!",
            "[Cliente]: Meu computador foi atacado. Preciso de um technopadre!",
            "[Demotech]: Mantenha a calma e diga o seu IP",
            "[Cliente]: XX.X.XXX.XX",
            "[Demotech]: Muito bem, agora é conosco.",
            "[Demotech]: Vamos exorcisar esses demônios o quanto antes do seu computador.",
        ]

        type(stdscr, dialog)

        stdscr.clear()
        stdscr.addstr(1, 1, "[u_002@demotech: ~]$ ")
        stdscr.refresh()
        time.sleep(1)

        connection_text = "scp -p 8910 ./exorcism.py root@XX.X.XXX.XX:~"
        for index, char in enumerate(connection_text):
            stdscr.addstr(1, 22 + index, char)
            stdscr.refresh()
            curses.napms(100)

        stdscr.addstr(2, 1, "[u_002@demotech: ~]$ ")
        stdscr.refresh()
        time.sleep(2)

        connection_text = "ssh -p 8910 root@XX.X.XXX.XX"
        for index, char in enumerate(connection_text):
            stdscr.addstr(2, 22 + index, char)
            stdscr.refresh()
            curses.napms(100)

        stdscr.addstr(3, 1, "Estabelecendo rotas")
        stdscr.refresh()
        time.sleep(1)
        stdscr.addstr(4, 1, "Conectando a XXX.X.XXX.XX IP na porta 8910.")
        stdscr.refresh()
        time.sleep(1)
        stdscr.addstr(5, 1, "Conexão estabelecida.")
        stdscr.refresh()
        time.sleep(3)

        stdscr.addstr(6, 1, "[root@lucy: ~]$ ")
        stdscr.refresh()
        time.sleep(2)

        connection_text = "./exorcism.py --full"
        for index, char in enumerate(connection_text):
            stdscr.addstr(6, 16 + index, char)
            stdscr.refresh()
            curses.napms(100)

        time.sleep(3)

        stdscr.clear()
        stdscr.addstr(height // 2 - 1, width // 2 - 11, "Carregando Exorcisador")
        stdscr.refresh()
        stdscr.addstr(height // 2 + 1, width // 2 - 13, "░░░░░░░░░░░░░░░░░░░░░░░░░░")

        connection_text = "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"
        for index, char in enumerate(connection_text):
            stdscr.addstr(height // 2 + 1, width // 2 - 13 + index, char)
            stdscr.refresh()
            curses.napms(100)

        cutscene_music.stop()

        time.sleep(1)

    stdscr.clear()

    virus_detected_sound = pygame.mixer.Sound("./audio/virus_detected.mp3")
    virus_detected_sound.play()
    stdscr.addstr(
        height // 2 - 1,
        width // 2 - 11,
        "10 Ameaças detectadas!",
    )
    stdscr.addstr(
        height // 2,
        width // 2 - 23,
        "Prepare-se para digitar os rituais de exorcismo",
    )
    stdscr.addstr(
        height // 2 + 1,
        width // 2 - 15,
        "Você tem 1 minuto e 30 segundos",
    )
    stdscr.refresh()
    time.sleep(5)

    stdscr.clear()
