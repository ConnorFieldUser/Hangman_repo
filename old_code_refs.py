HOMEWORK


Make a palindrome checker

Make program that know if the string is the same forwards or backwards


def pal():
    string = input("Type here: ")
    forwards = str(string.lower())
    backwards = str(string[::-1].lower())
    banned = ', :!.?'
    for thingy in banned:
        forwards = forwards.replace(thingy, '')
        backwards = backwards.replace(thingy, '')
    if forwards == backwards:
        return('Your phrase: ' + string + ', is a palindrome!')
    else:
        return('Your phrase: ' + string + ', is not a palindrome')

________________________________________________________________________________________________


Make a guessing game


def number_guesser():
    cpu_num = random.randint(1, 25)
    tries_left = 5
    for guess in range(5):
        player_guess = input("You have {} guesses left. Try to guess my number: ".format(tries_left))
        tries_left -= 1
        if cpu_num == int(player_guess):
            print("You win! The number was {}".format(cpu_num))
            break
        elif cpu_num > int(player_guess):
            print("Thats not it. My number is greater than that.")
        elif cpu_num < int(player_guess):
            print("Nope. My number is smaller than that.")
        elif player_guess != type.int:
            print("Numbers only")
    else:
        print("Game Over!")


number_guesser()


HARD MODE

import random


def computer_number_guesser():
    player_number = int(input("Pick a number between 1 and 25 for the computer to guess: "))
    tries_left = 5
    low = 0
    high = 25
    if player_number > 0 and player_number < 25:
        for guess in range(5):
            computer_guess = random.randint(low, high)
            tries_left -= 1
            if computer_guess == player_number:
                print("Computer wins! Your number was {}".format(player_number))
                break
            elif computer_guess > player_number:
                print("Lower")
                high = computer_guess
            elif computer_guess < player_number:
                print("Higher")
                low = computer_guess
            else:
                print("{}: Fail".format(computer_guess))
        else:
            print("Game Over. You win!")
    else:
        print("Between 1 and 25! Game over cheater.")

computer_number_guesser()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


WORD FREQUENCY



with open("sample.txt") as open_holmes:
    holmes = open_holmes.read()

holmes_scrubbed = holmes.lower()


loseit = ',.)(:\'#%$@]["!?/*;'
for stupid_thing_in_the_way in loseit:
    holmes_scrubbed = holmes_scrubbed.replace(stupid_thing_in_the_way, '').replace('\n', ' ')

holmes_scrubbed = holmes_scrubbed.split(' ')


words_in_holmes = {}

for wordin in holmes_scrubbed:
    if wordin in words_in_holmes.keys():
        words_in_holmes[wordin] += 1
    else:
        words_in_holmes[wordin] = 1

final_list = (sorted(words_in_holmes.items(), key=lambda x: x[1]))

final_list_20 = final_list[-21:-1]
final_list_20 = reversed(final_list_20)


for word, number in final_list_20:
    print(word + ': ' + str(number))




HARD MODE



with open("sample.txt") as open_holmes:
    holmes = open_holmes.read()

holmes_scrubbed = holmes.lower()


loseit = ',.)(:\'#%$@]["!?/*;'
for stupid_thing_in_the_way in loseit:
    holmes_scrubbed = holmes_scrubbed.replace(stupid_thing_in_the_way, '').replace('\n', ' ')

holmes_scrubbed = holmes_scrubbed.split(' ')


words_in_holmes = {}

bad_word = ['if', 'so', '', 'the', 'it', 'these', 'the', 'that', 'and', 'to', 'of', 'in', 'it', 'is', 'his']


for wordin in holmes_scrubbed:
    if wordin in holmes_scrubbed == bad_word:
        for bad in bad_word:
            holmes_scrubbed.replace(bad, '')
    elif wordin in words_in_holmes.keys():
        words_in_holmes[wordin] += 1
    else:
        words_in_holmes[wordin] = 1


final_list = (sorted(words_in_holmes.items(), key=lambda x: x[1]))

final_list_20 = final_list[-21:-1]
final_list_20 = reversed(final_list_20)

count = 0

for word, number in final_list_20:
    new_num = (number/50)
    print(word + ': ' + str(number) + '#' * new_num)



::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::



HANGMAN
