"""
Mark Jensen
Problem: Make a three door game
Certificate of Authenticity: I certify that this work is entirely my own
"""

from random import randint
from graphics import GraphWin, Rectangle, Point, Text, color_rgb
from button import Button


def main():
    win = GraphWin('Three Door Game', 400, 300)
    win.setCoords(0, 0, 100, 75)

    win.setBackground(color_rgb(randint(1, 255), randint(1, 255), randint(1, 255)))

    prompt = Text(Point(50, 70), "Select the secret door")
    prompt.draw(win)

    label_1 = "Door 1"
    rect_1 = Rectangle(Point(5, 30), Point(30, 45))
    button_1 = Button(rect_1, label_1)
    button_1.draw(win)

    label_2 = "Door 2"
    rect_2 = Rectangle(Point(37.5, 30), Point(62.5, 45))
    button_2 = Button(rect_2, label_2)
    button_2.draw(win)

    label_3 = "Door 3"
    rect_3 = Rectangle(Point(70, 30), Point(95, 45))
    button_3 = Button(rect_3, label_3)
    button_3.draw(win)

    button_list = [button_1, button_2, button_3]
    winner = button_list[randint(0, 2)]

    point = win.getMouse()
    prompt.undraw()

    if winner.is_clicked(point):
        winner.color_button("green")
        prompt.setText('You Win!')
        prompt.draw(win)
        win.getMouse()
        prompt.setText('Click anywhere to close')

    else:
        if button_1.is_clicked(point):
            button_1.color_button('red')

        if button_2.is_clicked(point):
            button_2.color_button('red')

        if button_3.is_clicked(point):
            button_3.color_button('red')

        lose_msg = Text(Point(50, 10), "You are one pathetic loser!" '\n' "The correct door was"
                        + " " + str(winner.get_label().lower()))
        lose_msg.draw(win)
        win.getMouse()
        lose_msg.setText('Click anywhere to close loser')

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
