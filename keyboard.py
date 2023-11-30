import curses


def initialize_keys():
    keys = {
        "KEY_COMMA": False,
        "KEY_PERIOD": False,
        "KEY_SPACE": False,
    }
    for char in "abcdefghijklmnopqrstuvwxyz":
        keys[f"KEY_{char.upper()}"] = False
    return keys


def draw_keyboard(stdscr, keys, height, width):
    key_positions = {
        "qwertyuiop": height - 12,
        "asdfghjkl": height - 9,
        "zxcvbnm,.": height - 6,
        "SPACE": height - 3,
    }

    test_values = [-68, -61, -55, -48]

    for row_chars, row_height, test_value in zip(
        key_positions.keys(), key_positions.values(), test_values
    ):
        test = test_value
        for char in row_chars:
            if char == ",":
                draw_keyboard_key(
                    stdscr,
                    keys["KEY_COMMA"],
                    char.upper(),
                    row_height,
                    width // 2 + test // 2,
                )
                test += 14
            elif char == ".":
                draw_keyboard_key(
                    stdscr,
                    keys["KEY_PERIOD"],
                    char.upper(),
                    row_height,
                    width // 2 + test // 2,
                )
                test += 14
            elif char == " ":
                draw_keyboard_key(
                    stdscr,
                    keys["KEY_SPACE"],
                    char.upper(),
                    row_height,
                    width // 2 + test // 2,
                )
                test += 14
            else:
                draw_keyboard_key(
                    stdscr,
                    keys[f"KEY_{char.upper()}"],
                    char.upper(),
                    row_height,
                    width // 2 + test // 2,
                )
                test += 14

        if row_chars == "SPACE":
            draw_keyboard_key(
                stdscr,
                keys["KEY_SPACE"],
                "SPACE",
                row_height,
                width // 2 - 48 // 2,
                5,
            )


def draw_keyboard_key(stdscr, is_pressed, key, y, x, padding=2):
    if is_pressed:
        stdscr.addstr(
            y,
            x,
            f"╭{'─' * (padding * len(key))}─{'─' * (padding * len(key))}╮",
            curses.color_pair(1),
        )
        stdscr.addstr(
            y + 1,
            x,
            f"│{' ' * ((padding * len(key)) - (len(key) // 2))}{key}{' ' * ((padding * len(key)) - (len(key) // 2))}│",
            curses.color_pair(1),
        )
        stdscr.addstr(
            y + 2,
            x,
            f"╰{'─' * (padding * len(key))}─{'─' * (padding * len(key))}╯",
            curses.color_pair(1),
        )
    else:
        stdscr.addstr(
            y, x, f"╭{'─' * (padding * len(key))}─{'─' * (padding * len(key))}╮"
        )
        stdscr.addstr(
            y + 1,
            x,
            f"│{' ' * ((padding * len(key)) - (len(key) // 2))}{key}{' ' * ((padding * len(key)) - (len(key) // 2))}│",
        )
        stdscr.addstr(
            y + 2, x, f"╰{'─' * (padding * len(key))}─{'─' * (padding * len(key))}╯"
        )


def handle_key_press(key_pressed, keys, key_pressed_audio):
    key_mapping = {
        ord(" "): "KEY_SPACE",
        ord(","): "KEY_COMMA",
        ord("."): "KEY_PERIOD",
    }
    for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        key_mapping[ord(char)] = "KEY_" + char.upper()

    if key_pressed in key_mapping:
        keys[key_mapping[key_pressed]] = True
        key_pressed_audio.play()
    elif key_pressed == 32:
        keys[key_mapping[key_pressed]] = True
        key_pressed_audio.play()
