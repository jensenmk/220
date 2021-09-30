"""
Mark Jensen

Problem: Create a greeting card

Certificate of authenticity: I ceritfy that this work is entirely my own
"""

from graphics import GraphWin, Circle, Text, Point, Polygon, Line, time, update


def main():
    win = GraphWin("Greeting Card", 400, 400, autoflush=False)
    win.setCoords(0, 0, 100, 100)
    win.setBackground("pink")
    circ = Circle(Point(70, 70), 10)
    circ.draw(win)
    circ.setFill("maroon")
    circ.setOutline("maroon")
    circ2 = circ.clone()
    circ2.draw(win)
    circ2.move(-20, 0)

    greet = Text(Point(50, 10), "Happy Valentines Day!")
    greet.draw(win)
    greet.setSize(24)
    greet.setFace("arial")
    greet.setTextColor("magenta")

    pt1 = Point(41.8, 64)

    pt2 = Point(78.05, 64)

    pt3 = Point(60, 70)

    pt4 = Point(60, 40)

    bottom = Polygon(pt1, pt4, pt2, pt3)
    bottom.draw(win)
    bottom.setFill("maroon")
    bottom.setOutline("maroon")

    pt6 = Point(65, 60)

    lp1 = Point(-40, -40)
    lp2 = Point(-20, -20)
    line = Line(lp1, lp2)
    line.draw(win)
    line.setWidth(10)

    line.setOutline("orange")
    line.setArrow("last")

    blo = Polygon(pt1, pt6, pt4)
    blo.draw(win)
    blo.setFill("maroon")
    blo.setOutline("maroon")

    for i in range(30):
        line.move(i, i)
        time.sleep(.1)
        update(120)

    greet.setText("Click anywhere to close")

    win.getMouse()


if __name__ == "__main__":
    main()
