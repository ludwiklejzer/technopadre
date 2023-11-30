import random

dragon = [
"             \\                  /              ",
"    _________))                ((__________    ",
"   /.-------./\\\\    \\    /    //\\.--------.\\   ",
"  //#######//##\\\\   ))  ((   //##\\\\########\\\\  ",
" //#######//###((  ((    ))  ))###\\\\########\\\\ ",
"((#######((#####\\\\  \\\\  //  //#####))########))",
" \\##' `###\######\\\\  \\)(/  //######/####' `##/ ",
"  )'    ``#)'  `##\\`->oo<-'/##'  `(#''     `(  ",
"          (       ``\\`..'/''       )           ",
"                     \\""(                      ",
"                      `- )                     ",
"                      / /                      ",
"                     ( /\\                      ",
"                     /\\| \\                     ",
"                    (  \\                       ",
"                        )                      ",
"                       /                       ",
"                      (                        ",
"                      `                        ",
]

mini = [
"            _.------.                        .----.__     ",
"           /         \\_.       ._           /---.__  \\    ",
"          |  O    O   |\\\\___  //|          /       `\\ |   ",
"          |  .vvvvv.  | )   `(/ |         | o     o  \\|   ",
"          /  |     |  |/      \\ |  /|   ./| .vvvvv.  |\\   ",
"         /   `^^^^^'  / _   _  `|_ ||  / /| |     |  | \\  ",
"       ./  /|         | O)  O   ) \\|| //' | `^vvvv'  |/\\\\ ",
"      /   / |         \\        /  | | ~   \\          |  \\\\",
"      \\  /  |        / \\ Y   /'   | \\     |          |   ~",
"       `'   |  _     |  `._/' |   |  \\     7        /     ",
"         _.-'-' `-'-'|  |`-._/   /    \\ _ /    .    |     ",
"    __.-'            \\  \\   .   / \\_.  \\ -|_/\\/ `--.|_    ",
" --'                  \\  \\ |   /    |  |              `-  ",
"                       \\uU \\UU/     |  /                  ",
        ]

twins = [
    "⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣷⣮⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⣻⣿⣿⣿⣿⣿⠂⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣷⠀⠀⠀⢀⣀⡀",
    "⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⢙⣿⣿⣿⣿⣿⣴⣶⣿⣿⣿⠇",
    "⠀⠀⠀⠀⠀⣾⣿⣿⣿⢸⣧⠁⠀⠀⠀⠀⠀⠀⠀⢀⣽⣧⣿⣿⣿⣿⣿⣿⡿⠋⠀",
    "⡀⠀⠀⠀⠀⢸⣿⣿⣿⣸⣿⣷⣄⠀⠀⠀⠀⠀⣰⣿⣿⢸⣿⣿⣿⣿⣿⡏⠀⠀⠀",
    "⠈⠫⠂⠀⠀⠊⣿⢿⣿⡏⣿⠿⠟⠀⠀⠀⠀⠈⠿⠿⣿⢸⣿⣿⣿⠛⠋⠀⠀⠀⠀",
    "⠀⠀⠀⠱⡀⠈⠁⠀⢝⢷⡸⡇⠀⠀⠀⠀⠀⠀⠀⢹⢣⡿⡙⠀⠉⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⢀⠇⠀⠀⢀⣾⣦⢳⡀⠀⠀⠀⠀⠀⠀⠀⢀⢟⣼⣧⡀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⢀⠎⠀⢀⣴⣿⣿⣿⡇⣧⠀⠀⠀⠀⠀⠀⠀⡾⣼⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀",
    "⢀⡔⠁⠀⢠⡟⢻⡻⣿⣿⣿⣌⡀⠀⠀⠀⠀⠀⢘⣠⣿⣿⣿⢟⠇⠀⠀⠀⠀⠀⠀",
    "⡎⠀⠀⠀⣼⠁⣼⣿⣦⠻⣿⣿⣷⡀⠀⠀⠀⢠⣿⣿⣿⢏⣴⣿⣇⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⡟⢰⣿⣿⡟⠀⠘⢿⣿⣷⡀⠀⢠⣿⣿⡿⠁⠀⢿⣿⣿⠀⠀⠀⠀⠀⠀",
    "⠳⠦⠴⠞⠀⢸⣿⣿⠁⠀⠀⠀⠹⣿⡧⠀⣾⣿⠏⠀⠀⠀⠘⣿⣿⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⢰⣿⡇⠀⢿⣿⡀⠀⠀⠀⠀⣽⣿⡄⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⢸⣿⡇⠀⢸⣿⡇⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⢸⣿⠁⠀⠀⠀⠀⢸⣿⡇⠀⢸⣿⠃⠀⠀⠀⠀⢸⣿⠇⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⡇⠀⢸⡿⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⣿⣆⠀⠀⠀⠀⠀⣿⣧⠀⣿⣧⠀⠀⠀⠀⠀⣼⣧⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠏⢿⠄⠀⠀⠀⠐⢸⣿⠀⣿⠇⠀⠀⠀⠀⢰⡿⠋⠀⠀⠀⠀⠀⠀",
]

skull2 = [
    "        .n                   .                 .                  n.         ",
    "  .   .dP                  dP                   9b                 9b.    .  ",
    " 4    qXb         .       dX                     Xb       .        dXp     t ",
    "dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb",
    "9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP",
    " 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP ",
    "  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'  ",
    "    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'    ",
    "        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~        ",
    "                        )b.  .dbo.dP'`v'`9b.odb.  .dX(                       ",
    "                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.                      ",
    "                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb                     ",
    "                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb                    ",
    "                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP                    ",
    "                     `'      9XXXXXX(   )XXXXXXP      `'                     ",
    "                              XXXX X.`v'.X XXXX                              ",
    "                              XP^X'`b   d'`X^XX                              ",
    "                              X. 9  `   '  P )X                              ",
    "                              `b  `       '  d'                              ",
]
skull = [
    "                  .xUHWH!! !!?M88WHX:.      ",
    "                .X*#M@$!!  !X!M$$$$$$WWx:.  ",
    "               :!!!!!!?H! :!$!$$$$$$$$$$8X: ",
    "              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:",
    "             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!",
    "             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!",
    '               !:~~~ .:!M"T#$$$$WX??#MRRMMM!',
    '               ~?WuxiW*`   `"#$$$$8!!!!??!!!',
    '             :X- M$$$$       `"T#$T~!8$WUXU~',
    "            :%`  ~#$$$m:        ~!~ ?$$$$$$ ",
    '          :!`.-   ~T$$$$8xx.  .xWW- ~""##*" ',
    ".....   -~~:<` !    ~?T#$$@@W@*?$$      /`  ",
    'W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :    ',
    '#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`    ',
    ':::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~     ',
    '.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `        ',
    'Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!           ',
    "$R@i.~~ !     :   ~$$$$$B$$en:``            ",
    '?MXT@Wx.~    :     ~"##*$$$$M~              ',
]

succubus = [
    "       ,;;;mMp'        l  ';mmmm;/  j       SSSMM;;           ",
    "     .;;;;;MM;         .\\,.mmSSSm,,/,      ,SSSMM;;;          ",
    "    ;;;;;;mMM;        .;MMmSSSSSSSmMm;     ;MSSMM;;;;         ",
    "   ;;;;;;mMSM;     ,_ ;MMmS;;;;;;mmmM;  -,;MMMMMMm;;;;        ",
    "  ;;;;;;;MMSMM;     \\\"*;M;( ( '') );m;*\"/ ;MMMMMM;;;;;,       ",
    " .;;;;;;mMMSMM;      \\(@;! _     _ !;@)/ ;MMMMMMMM;;;;;,      ",
    " ;;;;;;;MMSSSM;       ;,;.*o*> <*o*.;m; ;MMMMMMMMM;;;;;;,     ",
    ".;;;;;;;MMSSSMM;     ;Mm;           ;M;,MMMMMMMMMMm;;;;;;.    ",
    ";;;;;;;mmMSSSMMMM,   ;Mm;,   '-    ,;M;MMMMMMMSMMMMm;;;;;;;   ",
    ";;;;;;;MMMSSSMMMMMMMm;Mm;;,  ___  ,;SmM;MMMMMMSSMMMM;;;;;;;;  ",
    ';;\'";;;MMMSSSSMMMMMM;MMmS;;,  "  ,;SmMM;MMMMMMSSMMMM;;;;;;;;. ',
    "!   ;;;MMMSSSSSMMMMM;MMMmSS;;._.;;SSmMM;MMMMMMSSMMMM;;;;;;;;; ",
    "    ;;;;*MSSSSSSMMMP;Mm*\"'q;'   `;p*\"*M;MMMMMSSSSMMM;;;;;;;;; ",
    "    ';;;  ;SS*SSM*M;M;'     `-.        ;;MMMMSSSSSMM;;;;;;;;;,",
    "     ;;;. ;P  `q; qMM.                 ';MMMMSSSSSMp' ';;;;;;;",
    "     ;;;; ',    ; .mm!     \\.   `.   /  ;MMM' `qSS'    ';;;;;;",
    "     ';;;       ' mmS';     ;     ,  `. ;'M'   `S       ';;;;;",
    "      `;;.        mS;;`;    ;     ;    ;M,!     '  luk   ';;;;",
    "       ';;       .mS;;, ;   '. o  ;   oMM;                ;;;;",
]

pentagram = [
    "                (,.' ..' .)-..            ,.-( `.. `.. )                   ",
    "                 (,.' ,.'  ..')-.     ,.-( `. `.. `.. )                    ",
    "                  (,.'  ,.' ,.'  )-.-('   `. `.. `.. )                     ",
    "                   ( ,.' ,.'    _== ==_     `.. `.. )                      ",
    "                    ( ,.'   _==' ~  ~  `==_    `.. )                       ",
    "                     \\  _=='   ----..----  `==_   )                        ",
    "                  ,.-:    ,----___.  .___----.    -..                      ",
    "              ,.-'   (   _--====_  \\/  _====--_   )  `-..                  ",
    "          ,.-'   .__.'`.  `-_I0_-'    `-_0I_-'  .'`.__.  `-..              ",
    "      ,.-'.'   .'      (          |  |          )      `.   `.-..          ",
    "  ,.-'    :    `___--- '`.__.    / __ \\    .__.' `---___'    :   `-..      ",
    "-'_________`-____________'__ \\  (O)  (O)  / __`____________-'________`-     ",
    "                            \\ . _  __  _ . /                                ",
    "                             \\ `V-'  `-V' |                                 ",
    "                              | \\ \\ | /  /                                  ",
    "                               V \\ ~| ~/V                                   ",
    "                                |  \\  /|                                    ",
]

devil = [
    "       ___,---.__          /'|`\\          __,---,___          ",
    "    ,-'    \\`    `-.____,-'  |  `-.____,-'    //    `-.       ",
    "  ,'        |           ~'\\     /`~           |        `.     ",
    " /      ___//              `. ,'          ,  , \\___      \\    ",
    "|    ,-'   `-.__   _         |        ,    __,-'   `-.    |   ",
    "|   /          /\\_  `   .    |    ,      _/\\          \\   |   ",
    "\\  |           \\ \\`-.___ \\   |   / ___,-'/ /           |  /   ",
    " \\  \\           | `._   `\\\\  |  //'   _,' |           /  /    ",
    "  `-.\\         /'  _ `---'' , . ``---' _  `\\         /,-'     ",
    "     ``       /     \\    ,='/ \\`=.    /     \\       ''        ",
    "             |__   /|\\_,--.,-.--,--._/|\\   __|                ",
    "             /  `./  \\\\`\\ |  |  | /,//' \\,'  \\                ",
    "            /   /     ||--+--|--+-/-|     \\   \\               ",
    "           |   |     /'\\_\\_\\ | /_/_/`\\     |   |              ",
    "            \\   \\__, \\_     `~'     _/ .__/   /               ",
    "             `-._,-'   `-._______,-'   `-._,-'                ",
]

faun = [
    "   )       (\\___/)     (  ",
    "* /(       \\ (. .)     )\\ *",
    "  # )      c\\   >'    ( # ",
    "   '         )-_/      '  ",
    " \\\\|,    ____| |__    ,|//",
    "   \\ )  (  `  ~   )  ( /  ",
    "    #\\ / /| . ' .) \\ /#   ",
    "    | \\ / )   , / \\ / |   ",
    "     \\,/ ;;,,;,;   \\,/    ",
    "      _,#;,;;,;,          ",
    "     /,i;;;,,;#,;         ",
    "    //  %;;,;,;;,;        ",
    "   ((    ;#;,;%;;,,       ",
    "  _//     ;,;; ,#;,       ",
    " /_)      #,;    ))       ",
    "         //      \\|_     ",
    "         \\|_      |#\\   ",
    '          |#\\      -"    ',
]


def clear_ascii_demon(stdscr, ascii_art):
    height, width = stdscr.getmaxyx()

    for index, line in enumerate(ascii_art):
        stdscr.addstr(
            1 + index, width // 2 - (len(max(ascii_art, key=len)) // 2), " " * len(line)
        )


def print_demon_ascii(stdscr, ascii_art):
    height, width = stdscr.getmaxyx()

    for index, line in enumerate(ascii_art):
        stdscr.addstr(
            height - len(ascii_art) - 15 + index,
            width // 2 - (len(max(ascii_art, key=len)) // 2),
            line,
        )


def print_demon_life(stdscr, life):
    height, width = stdscr.getmaxyx()
    stdscr.addstr(height // 2 - 6, width - 5, "Demon")

    bar_size = life // 10  # Calcula o tamanho da barra proporcional à vida

    for i in range(height // 2 - 5, (height // 2 - 5) + 10):
        if i < (height // 2 - 5) + bar_size:
            stdscr.addstr(i, width - 3, "██")
        else:
            stdscr.addstr(i, width - 3, "░░")


def get_demon(level, demon_before=None):
    level_1_demons = [
        {"life": 100, "damage": 5, "ascii": faun},
        {"life": 100, "damage": 30, "ascii": twins},
        {"life": 140, "damage": 10, "ascii": skull},
        {"life": 120, "damage": 15, "ascii": skull2},
        {"life": 250, "damage": 50, "ascii": dragon},
        {"life": 200, "damage": 40, "ascii": pentagram},
        {"life": 150, "damage": 15, "ascii": devil},
        {"life": 180, "damage": 20, "ascii": succubus},
    ]

    if level == 1:
        chosen_demon = random.choice(level_1_demons)
        while demon_before and demon_before.get("ascii") == chosen_demon.get("ascii"):
            chosen_demon = random.choice(level_1_demons)

        return chosen_demon
