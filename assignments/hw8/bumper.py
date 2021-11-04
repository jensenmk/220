"""
Mark Jensen
problem: create a bumper car simulation
Certificate of Authenticity: I certify that this work is entirely my own
"""

import math
from random import randint
from graphics import GraphWin, Circle, Point, color_rgb, update


def get_random(move_amount):
    num = 0
    while num == 0:
        num = randint(-move_amount, move_amount)
    return num


def did_collide(circle1, circle2):
    center1 = circle1.getCenter()
    center1_x, center1_y = center1.getX(), center1.getY()

    center2 = circle2.getCenter()
    center2_x, center2_y = center2.getX(), center2.getY()

    hyp = math.sqrt((center1_x - center2_x) ** 2 + (center1_y - center2_y) ** 2)
    dist = circle1.getRadius() * 2
    if hyp <= dist:
        return True
    return False


def hit_vertical(circle, win):
    center = circle.getCenter()
    c_x = center.getX()
    if win.width - abs(c_x) <= circle.getRadius():
        return True
    if c_x <= circle.getRadius():
        return True
    return False


def hit_horizontal(circle, win):
    center = circle.getCenter()
    c_y = center.getY()
    if win.height - abs(c_y) <= circle.getRadius():
        return True
    if c_y <= circle.getRadius():
        return True
    return False


def get_random_color():
    random_color = color_rgb(randint(1, 255), randint(1, 255), randint(1, 255))
    return random_color


def main():
    # create window
    win = GraphWin('bumper', 600, 400)
    win.setCoords(0, 0, 600, 400)
    win.setBackground(get_random_color())

    # create circle 1
    c_1 = Circle(Point(randint(20, 280), randint(20, 280)), 20)
    c_1.draw(win)
    c_1.setFill(get_random_color())

    # initial direction of circle 1
    d1x = get_random(1)
    d1y = get_random(1)

    # create circle 2
    c_2 = Circle(Point(randint(20, 280), randint(20, 280)), 20)
    c_2.draw(win)
    c_2.setFill(get_random_color())

    # initial direction of circle 2
    d2x = get_random(1)
    d2y = get_random(1)

    while win.checkMouse() != '':
        # c1 movement and rules
        c_1.move(d1x, d1y)
        if hit_vertical(c_1, win):
            d1x = -d1x
        if hit_horizontal(c_1, win):
            d1y = -d1y

        # c2 movement and rules
        c_2.move(d2x, d2y)
        if hit_vertical(c_2, win):
            d2x = -d2x
        if hit_horizontal(c_2, win):
            d2y = -d2y

        update(randint(300, 500))
        # check for collision
        if did_collide(c_1, c_2):
            d1x = -d1x
            d1y = -d1y
            d2x = -d2x
            d2y = -d2y

        if win.checkMouse() is not None:
            break

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
