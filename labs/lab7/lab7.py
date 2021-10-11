"""
Name: Mark Jensen
Partner: <your partner's name goes here – first and last>
lab7.py
"""

import math


def main():
    print(sphere_area(2))
    print(sphere_volume(2))
    print(sum_n(5))
    print(sum_n_cubes(3))
    pass


def cash_conversion():
    dollar_amt = int(input('Enter an integer: '))
    print("${:.2f}".format(dollar_amt))


def encode():
    msg = input('enter message: ')
    key = int(input('enter an integer key: '))
    acc = ''
    for c in msg:
        i = ord(c)
        k = i + key
        new_char = chr(k)
        acc += new_char
    print(acc)


def sphere_area(radius):
    area = 4 * math.pi * radius ** 2
    return area


def sphere_volume(radius):
    volume = (4/3) * math.pi * radius ** 3
    return volume


def sum_n(n):
    acc = 0
    for i in range(n):
        acc += i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc += i ** 3
    return acc


def encode_better():
    msg = input('enter message to encode: ')
    key = input('enter a key: ')
    acc = ''
    for i in range(len(msg)):
        c = ord(msg[i])
        k = ord(key[i])
        result = c + k - 97
        acc += chr(result)
    print(acc)




#sphere_volume
#sphere_area
#cash_conversion()
#encode()
#encode_better()
#main()

