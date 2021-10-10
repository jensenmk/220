"""
Mark Jensen

Problem: Create a vigenere cypher

Certificate of Authenticity: I certify that this work is entirely my own
"""

from graphics import *


def code(message, key):
    # get message and key from user
    msg = message.upper().split(" ")
    msg = "".join(msg)
    ki = key.upper()

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # convert message and key to numbers in letters string
    msg_list = []
    for i in msg:
        msg_num = letters.find(i)
        msg_list.append(int(msg_num))

    key_list = []
    for i in ki:
        key_num = letters.find(i)
        key_list.append(int(key_num))

    # add consecutive digits together in msg_list and key_list
    comp_list = []
    for i in range(len(msg_list)):
        comp = msg_list[i] + key_list[i % len(key_list)]
        comp_list.append(int(comp))

    # convert comp_list back to letters
    result = ""
    for i in range(len(comp_list)):
        result = result + letters[comp_list[i] % len(letters)]

    return result


def main():
    # Make graphics window
    win = GraphWin('Vigenere', 450, 300)
    win.setCoords(0, 0, 100, 65)
    win.setBackground('light grey')

    # Message input box
    inst1 = Text(Point(20, 55), 'Message to code')
    inst1.draw(win)
    msg = Entry(Point(60, 55), 35)
    msg.draw(win)

    # keyword input box
    inst2 = Text(Point(21, 40), 'Enter Keyword')
    inst2.draw(win)
    ki = Entry(Point(44.5, 40), 15)
    ki.draw(win)

    # dummy button
    button = Rectangle(Point(35, 20), Point(65, 30))
    button.draw(win)
    userclick = Text(Point(50, 25), "Encode")
    userclick.draw(win)

    win.getMouse()

    # call function
    result = code(msg.getText(), ki.getText())

    userclick.undraw()
    button.undraw()

    msg_prnt = Text(Point(50, 25), "Resulting Message \n" + result)
    msg_prnt.draw(win)

    key_prnt = Text(Point(50, 5), "Click Anywhere To Close Window")
    key_prnt.draw(win)

    win.getMouse()
    win.close()


main()
