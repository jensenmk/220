"""
Name: Mark Jensen
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("volume =", volume)

def shooting_percentage():
    shots = eval(input("Shots attempted: "))
    shots_made = eval(input("Shots made: "))
    shooting_percentage = shots_made/shots * 100
    print("shooting percentage =", shooting_percentage)

def coffee():
    pounds = eval(input("Pounds of coffee purchased: "))
    total_cost = 10.5 * pounds + .86 * pounds + 1.50
    print("Total Cost =", total_cost)

def kilometers_to_miles():
    kilometers = eval(input("Kilometers: "))
    miles = kilometers/1.61
    print("Miles= ", miles)




calc_rec_area()
calc_volume()
shooting_percentage()
coffee()
kilometers_to_miles()