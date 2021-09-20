"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to place square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(190, 190), Point(210, 210))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of circle
        shape_2 = shape.clone()
        shape_2.draw(win)
        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)

    inst_pt_2 = Point(width / 2, height - 390)
    instructions2 = Text(inst_pt_2, "Click anywhere to exit")
    instructions2.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)
    inst_pt3 = Point(200, 390)
    instructions3 = Text(inst_pt3, "Click upper left and lower right of desired rectangle")
    instructions3.draw(win)
    user_click = win.getMouse()
    user_click2 = win.getMouse()
    shape = Rectangle(Point(user_click.x, user_click.y), Point(user_click2.x, user_click2.y))
    shape.setFill("blue")
    shape.draw(win)

    width = abs(user_click.y - user_click2.y)
    length = abs(user_click.x - user_click2.x)

    area = width * length
    ach_pnt = Point(50, 10)
    area_1 = Text(ach_pnt, "Area = " + str(area))
    area_1.draw(win)

    perm = 2 * width + 2 * length
    ach_pnt_2 = Point(330, 10)
    perm_1 = Text(ach_pnt_2, "Perimeter = " + str(perm))
    perm_1.draw(win)

    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Circle Radius", width, height)

    u_i = win.getMouse()
    u_i2 = win.getMouse()
    x1 = u_i.getX()
    x2 = u_i2.getX()
    y1 = u_i.getY()
    y2 = u_i2.getY()
    r = (((x1-x2) ** 2) + ((y1 - y2) ** 2)) ** (1/2)

    crc = Circle(u_i, r)
    crc.setFill("blue")
    crc.draw(win)

    ach_pnt = Point(200, 390)
    crc_1 = Text(ach_pnt, "Radius = " + str(r))
    crc_1.draw(win)

    ach_pnt2 = Point(200, 10)
    inst = Text(ach_pnt2, "Click anywhere to close")
    inst.draw(win)

    win.getMouse()
    win.close()


def pi2():
    import math
    n = eval(input("number of terms in a series "))
    acc = 0
    for i in range(n):
        num = 4
        denom = 1 + (2 * i)
        frac = (num / denom) * ((-1) ** i)
        acc = acc + frac
    print(acc)
    print(math.pi - acc)


def main():

    # squares()
    # rectangle()
    # circle()
    # pi2()


main()
