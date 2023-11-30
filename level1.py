import curses
import random
import pygame
import datetime
import time
from keyboard import draw_keyboard, handle_key_press, initialize_keys
from cutscene1 import cutscene1
from demon import get_demon, print_demon_ascii, print_demon_life, clear_ascii_demon
from player import print_user_life


def level1(stdscr, is_first_time):
    cutscene1(stdscr, is_first_time)
    height, width = stdscr.getmaxyx()
    keys = initialize_keys()
    demon = get_demon(1)
    demons_defeated = 0

    now = datetime.datetime.now()
    target_time = now + datetime.timedelta(minutes=1.5)

    player = {"life": 100}

    pygame.init()
    key_pressed_audio = pygame.mixer.Sound("./audio/key_pressed.wav")
    demon_death_sound = pygame.mixer.Sound("./audio/demon_death.wav")
    player_damage_sound = pygame.mixer.Sound("./audio/player_damage.mp3")
    game_over_sound = pygame.mixer.Sound("./audio/game_over.mp3")
    level1_music = pygame.mixer.Sound("./audio/level1_music.wav")
    level1_music.play(loops=-1)
    level1_music.set_volume(0.3)

    sentences = [
        "Ab insidiis diaboli, libera nos, Domine.",
        "Vade, Satana, inventor et magister omnis fallaciae, hostis humanae salutis.",
        "Omnis incursio infernalis adversarii, omnis legio, omnis congregatio et secta diabolica.",
        "Ergo, draco maledicte, ecclesiam tuam securi tibi facias libertate servire.",
        "Exorcizamus te, omnis immundus spiritus, omnis satanica potestas.",
        "In nomine Patris, et Filii, et Spiritus Sancti.",
        "Exsurgat Deus et dissipentur inimici ejus: et fugiant qui oderunt eum a facie ejus.",
        "Sicut deficit fumus deficiant, sicut fluit cera a facie ignis, sic pereant peccatores a facie Dei.",
    ]
    original_sentence = sentences[random.randint(0, len(sentences) - 1)]
    typed_sentence = ""

    stdscr.addstr(
        height - 14, width // 2 - len(original_sentence) // 2, original_sentence
    )

    while True:
        print_demon_ascii(stdscr, demon["ascii"])
        print_user_life(stdscr, player["life"])
        print_demon_life(stdscr, demon["life"])

        remaining_time = target_time - datetime.datetime.now()
        timer_display = remaining_time - datetime.timedelta(
            microseconds=remaining_time.microseconds
        )

        stdscr.addstr(0, 0, f"Tempo restante: {timer_display}")
        stdscr.refresh()

        key_pressed = stdscr.getch()
        draw_keyboard(stdscr, keys, height, width)
        keys = {key: False for key in keys}
        handle_key_press(key_pressed, keys, key_pressed_audio)

        if 32 <= key_pressed <= 126:
            typed_sentence += chr(key_pressed)
            if chr(key_pressed) == original_sentence[len(typed_sentence) - 1]:
                demon["life"] -= 5
                stdscr.addstr(
                    height - 14,
                    (width // 2 - len(original_sentence) // 2)
                    + (len(typed_sentence) - 1),
                    chr(key_pressed),
                    curses.color_pair(2) | curses.A_STANDOUT,
                )
            else:
                player["life"] -= demon["damage"]
                player_damage_sound.play()
                stdscr.addstr(
                    height - 14,
                    (width // 2 - len(original_sentence) // 2)
                    + (len(typed_sentence) - 1),
                    chr(key_pressed),
                    curses.color_pair(1) | curses.A_STANDOUT,
                )

        if len(typed_sentence) == len(original_sentence):
            stdscr.addstr(height - 14, 0, f"{' ' * width}")  # fake clear
            original_sentence = sentences[random.randint(0, len(sentences) - 1)]
            stdscr.addstr(
                height - 14, width // 2 - len(original_sentence) // 2, original_sentence
            )
            typed_sentence = ""

        if demon["life"] == 0:
            demon_death_sound.play()
            clear_ascii_demon(stdscr, demon["ascii"])
            demons_defeated += 1
            demon = get_demon(1, demon)

        if datetime.datetime.now() >= target_time:
            stdscr.clear()
            stdscr.addstr(height // 2 - 1, width // 2 - 5, "Game Over!")
            stdscr.refresh()
            stdscr.clear()
            player["life"] = 100
            level1_music.stop()
            time.sleep(3)
            break
        if player["life"] <= 0:
            game_over_sound.play()
            stdscr.clear()
            stdscr.addstr(height // 2 - 1, width // 2 - 5, "Game Over!")
            stdscr.refresh()
            stdscr.clear()
            player["life"] = 100
            level1_music.stop()
            time.sleep(3)
            break
        if demons_defeated == 10:
            stdscr.clear()
            stdscr.addstr(height // 2 - 1, width // 2 - 7, "Missão cumprida")
            stdscr.addstr(
                height // 2, width // 2 - 17, "Todos os demônios foram exorcisados"
            )
            stdscr.refresh()
            stdscr.clear()
            level1_music.stop()
            time.sleep(5)
            demons_defeated = 0
            break
