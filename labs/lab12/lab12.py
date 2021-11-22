"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
from random import randint


def main():
    lst = [1, 2, 3, 4, 5, 6]

    find_and_remove_first(lst, 3)
    is_in_linear(2, lst)
    good_input()
    num_digits()
    hi_lo_game()


def find_and_remove_first(list, value):
    try:
        i = list.index(value)
        list[i] = "Mark"
        print(list)
    except:
        pass


def read_data(file):
    f = open(file, 'r')
    data = f.read()
    data = data.split()
    return data


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == values[i]:
            return True
        i += 1
    return False


def good_input():
    x = eval(input('enter a number between 1 and 10'))
    while x < 1 or x > 10:
        x = eval(input('enter a number between 1 and 10'))
    return x


def num_digits():
    num = eval(input('enter a number 1 or greater: '))
    while num >= 1:
        digits = 0
        while num != 0:
            num //= 10
            digits += 1
        print("the number of digits are", digits)
        num = eval(input('enter a number 1 or greater: '))


def hi_lo_game():
    secret = randint(1, 100)
    guess = 1
    num = eval(input("guess the secret number between 1 and 100: "))
    while num != secret and guess < 7:
        guess += 1
        if num > secret:
            print('too high')
        else:
            print('too low')
        num = eval(input('guess again: '))
    if num == secret:
        print('you guessed correct in', guess, 'guesses')
    else:
        print('you lose!')







main()
