
import random


man8 = "START"

man7 = """
_____________
"""

man6 = """
|
|
|
|
|____________
|
"""


man5 = """
---
|
|
|     |
|
|_____________
|
"""


man4 = """
-----
|
|
|     |
|    / \\
|______________
|
"""


man3 = """
---------
|
|
|    -|-
|    / \\
|______________
|
"""


man2 = """
-----------
|
|     O
|    -|-
|    / \\
|______________
|
"""


man1 = """
--/--------|
|/
|     O
|    -|-
|    / \\
|______________
|
|ONE TRY LEFT!!!
"""

man0 = """
--/----|----|
|/     |
|      O
|     -|-
|     / \\
|___       ______
|   \     /
|YOU DIED
"""


man_fail = """
    _
    0
   -|-
   / \\
~~ ~~~~~~ ~~~

"""

man_stages = [man0, man1, man2, man3, man4, man5, man6, man7, man8]

# for stage in man_stages:
#    print stage

with open("/usr/share/dict/words") as open_text:
    formated_text = open_text.read()

formated_text = formated_text.lower()
formated_text = formated_text.split()


def menu():
    q = input("Play again? y/n: ").lower()
    if q == "y":
        diff_prompt()
    else:
        print("Thanks for playing. Bye")

easy = []
normal = []
hard = []

for find in formated_text:
    if len(find) > 3 and len(find) < 7:
        easy.append(find)
    elif len(find) > 7 and len(find) < 10:
        normal.append(find)
    elif len(find) > 10:
        hard.append(find)
# print(hard)


def diff_prompt():
    diff_set = input("Easy:e Normal:n Hard:h >>>").lower()
    if diff_set == 'e':
        hidden_word = random.choice(easy)
        hangman_game(hidden_word)
    elif diff_set == 'n':
        hidden_word = random.choice(normal)
        hangman_game(hidden_word)
    elif diff_set == 'h':
        hidden_word = random.choice(hard)
        hangman_game(hidden_word)
    else:
        print("E, N, H: ")
        diff_prompt()


def hangman_game(hidden_word):
    print("Welcome to Hangman!")

    # hidden_word = random.choice()

    # rand_num = random.randint(1, 235886)
    # hidden_word = formated_text[rand_num]
    # hidden_word = str(hidden_word)
    #  print(hidden_word)
    # diff_prompt()

    word_len = len(hidden_word)
    print("The word is {} letters long.".format(word_len))

    print(man8)
    letters_not_guessed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                           'w', 'x', 'y', 'z']
    turns = 8
    progress = []
    punctuation = "., /\[]{}+_)(*&^%$#@!~`1234567890-=|?<>:;`)"

    for instance in range(word_len):
        progress.append('_')

    while turns > 0:
        # print("_ " * word_len)
        string_progress = (''.join(progress))
        if hidden_word == str(string_progress):
            print("You win!! Your word was {}".format(hidden_word))
            break

        print("You have {} turns left".format(str(turns)))
        print(string_progress)
        player_letter = input("""Pick a letter, type STATUS to see your status, LETTERS to see unused letters, or END
to quit: """).lower()
        if player_letter == "end":
            print("goodbye")
            break
        elif player_letter == "letters":
            print(str(letters_not_guessed))
            continue
        elif player_letter == 'status':
            print(man_stages[turns])
            continue
        elif len(player_letter) > 1:
            print("Only single letters please")
            continue
        elif player_letter in punctuation:
            print("Only single letters please")
            continue
        elif player_letter in letters_not_guessed:
            letters_not_guessed.remove(player_letter)
        else:
            print("You've already guessed that letter!")
            continue
        print("letters remaining: " + str(letters_not_guessed))
        if player_letter in hidden_word:
            print("CORRECT")
            for letter_index, let_in_HW in enumerate(hidden_word):
                if let_in_HW == player_letter:
                    del progress[letter_index]
                    progress.insert(letter_index, let_in_HW)
            continue
        else:
            print("WRONG LETTER")
            turns -= 1
            print(man_stages[turns])
    else:
        print(man_fail + "The word was: {}".format(hidden_word))

    menu()

diff_prompt()

# hangman_game()
