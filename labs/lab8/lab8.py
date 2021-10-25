"""
Name: Mark Jensen
lab8.py
"""

from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w+')
    i = 1
    for line in in_file:
        words = line.split()
        for word in words:
            out_file.write(str(i) + ' ' + word + '\n')
            i = i + 1
    in_file.close()
    out_file.close()


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w+')
    for line in in_file:
        parts = line.split()
        wage = float(parts[2])
        wage += 1.65
        wage = wage * int(parts[3])
        out_file.write(parts[0] + ' ' + parts[1] + ' ' + str(wage) + '\n')


def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc += int(isbn[i]) * pos
    return acc


def send_message(file, friend):
    in_file = open(file, 'r')
    out_file = open(friend + '.txt', 'w+')
    for line in in_file:
        out_file.write(line)


def send_safe_message(file, friend, key):
    in_file = open(file, 'r')
    out_file = open(friend + '.txt', 'w+')
    for line in in_file:
        out_file.write(encode(line, key))


def send_uncrackable_message(file, friend, pad):
    in_file = open(file, 'r')
    out_file = open(friend + '.txt', 'w+')
    pad_file = open(pad, 'r')
    key = pad_file.read()
    for line in in_file:
        out_file.write(encode_better(line, key))


def main():
    # number_words("Walrus.txt", "outfile.txt" )
    # hourly_wages("hourly_wages.txt", "outfile.txt")
    # print(calc_check_sum("0072946520"))
    # send_message('secret_message.txt', 'mark')
    # send_safe_message('secret_message.txt', 'mark', 123)
    # send_uncrackable_message('secret_message.txt', 'mark', 'pad.txt')

    pass


main()
