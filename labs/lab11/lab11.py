"""
Name: Mark Jensen
hangman.py
"""

from random import randint


def main():
    play()
    pass


def words(file_name):
    in_file = open(file_name, 'r')
    content = in_file.read()
    return content.split('\n')


def rand_word(word_list):
    return word_list[randint(0, len(word_list)-1)]


def fill(word, letters):
    secret = ["_"] * len(word)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return ''.join(secret)


def won(word, letters):
    secret = fill(word, letters)
    if secret == word:
        return True
    else:
        return False


def play():
    word_list = words('wordlist.txt')
    secret = rand_word(word_list)
    incorrect = 0
    guesses = []
    while not won(secret, guesses) and incorrect <= 7:
        display = fill(secret, guesses)
        print(display)
        print(guesses)
        letter = input('enter guess: ')
        while letter in guesses:
            letter = input("enter a letter you haven't entered yet")
        guesses.append(letter)
        display = fill(secret, guesses)
        if guesses != display:
            incorrect += 1
        else:
            guesses = display


main()
