"""
Mark Jensen
I certify that this work is entirely my own
"""

from graphics import Text


class Button:
    """Creates a button with centered text, takes a rectangle and a string"""
    def __init__(self, shape, text):
        self.shape = shape
        self.text = Text(self.shape.getCenter(), text)
        p_1 = self.shape.getP1()
        p_2 = self.shape.getP2()
        self.p1_x = p_1.getX()
        self.p1_y = p_1.getY()
        self.p2_x = p_2.getX()
        self.p2_y = p_2.getY()

    def get_label(self):
        """Return: button text as string"""
        return self.text.getText()

    def draw(self, win):
        """Draws button with text"""
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        """Undraws button and text"""
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        """returns true if mouse clicked within button"""
        return (self.p1_x <= point.getX() <= self.p2_x
                and self.p1_y <= point.getY() <= self.p2_y)

    def color_button(self, color):
        """Sets button color"""
        self.shape.setFill(color)

    def set_label(self, text):
        """sets button label"""
        self.text = Text(self.shape.getCenter(), text)
