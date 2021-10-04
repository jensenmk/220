"""
Name: Mark Jensen
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    first, last = input('Enter name in first last order: ').split()
    print(last + ", " + first)


def company_name():
    first, second, third = input("Enter website name: ").split(".")
    print(second)


def initials():
    num_names = int(input("How many students in class? "))
    for i in range(num_names):
        first = input("Enter the first name of student " + str(i + 1) + ": ")
        last = input("Enter " + first + "'s last name: ")
        print(first + "'s initials are " + first[0] + last[0] + ".")


def names():
    names = input("Enter a list of names, first and last separated by a comma: ")
    names = names.split(", ")
    for i in names:
        name_list = i.split(" ")
        first = name_list[0][0]
        last = name_list[1][0]
        print(first + last)


def thirds():
    sent = int(input('How many sentences will be input? '))
    for i in range(sent):
        sentence = input("enter sentence: ")
        print(sentence[2::3])


def word_average():
    sent = (input('Enter a sentence: '))
    sent = sent.split()
    acc = 0
    for word in sent:
        acc = acc + len(word)
    avg = acc / len(sent)
    print(avg)


def pig_latin():
    sent = input('Enter a sentence: ')
    sent = sent.lower()
    sent = sent.split()
    for word in sent:
        x = word[1:]
        word = x + word[0] + "ay"
        print(word, end=" ")


def main():
    #name_reverse()
    #company_name()
    #initials()
    #names()
    #thirds()
    #word_average()
    #pig_latin()

main()
