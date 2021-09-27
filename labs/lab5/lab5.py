"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()

import math

def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    l1 = Line(p1, p2)
    l2 = Line(p2, p3)
    l3 = Line(p3, p1)

    p1x = p1.getX()
    p1y = p1.getY()
    p2x = p2.getX()
    p2y = p2.getY()
    p3x = p3.getX()
    p3y = p3.getY()

    d1 = ((p1x - p2x) ** 2 + (p1y - p2y) ** 2) ** (1/2)
    d2 = ((p2x - p3x) ** 2 + (p2y - p3y) ** 2) ** (1/2)
    d3 = ((p3x - p1x) ** 2 + (p3y - p1y) ** 2) ** (1/2)

    perimeter = d1 + d2 + d3
    s = perimeter / 2
    area = (s * (s - d1) * (s - d2) * (s - d3)) ** (1/2)
    pt = Point(250, 490)
    pt2 = Point(250, 470)
    inst = Text(pt, "perimeter = " + str(perimeter))
    inst2 = Text(pt2, 'area = ' + str(area))
    l1.draw(win)
    l2.draw(win)
    l3.draw(win)
    inst.draw(win)
    inst2.draw(win)
    # inst.draw(win)
    # and display its area in the graphics window.

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_entry = Entry(Point(win_width / 2, win_height / 2 + 40), 5)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_entry = Entry(Point(win_width / 2, win_height / 2 + 70), 5)
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_entry = Entry(Point(win_width / 2, win_height / 2 + 100), 5)
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    red_entry.draw(win)
    blue_entry.draw(win)
    green_entry.draw(win)

    win.getMouse()
    for i in range(5):
        red_num = int(red_entry.getText())
        blue_num = int(blue_entry.getText())
        green_num = int(green_entry.getText())
        color = color_rgb(red_num, green_num, blue_num)
        shape.setFill(color)
        win.getMouse()



    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    s = input("enter text")
    print(s[0])
    print(s[-1])
    print(s[2:6])
    print(s[0] + s[-1])
    print(s[0:3] * 10)
    for i in range(len(s)):
        print(s[i])
    print(len(s))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = str(values[2]),  str(values[3]),  str(values[4])
    print(x)
    x = str(values[2]), str(values[3]),  str(values[0])
    print(x)
    x = values[2], values[0], float(values[5])
    print(x)
    x = values[2] + values[0] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    n = eval(input("number of terms"))
    s = 0
    for i in range(n):
        y = 2 + (2 * (i % 3))
        print(y, end=" ")
        s = y + s
    print(s)






def main():
    # target()
    triangle()
    # color_shape()
    # process_string()
    # process_list()
    # another_series()
    pass





main()
