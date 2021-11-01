"""
Name: Mark Jensen
lab9.py
"""

from graphics import *
import math


def addTen(nums):
    num_list = []
    for i in nums:
        num = int(i) + 10
        num_list.append(num)
    print(num_list)


def squareEach(nums):
    print(nums)
    sum = 0
    for i in nums:
        nums = int(i) ** 2
        sum = int(nums) + int(sum)
    print(sum)


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    return acc


def toNumbers(strNums):
    for i in range(len(strNums)):
        strNums[i] = float(strNums[i])


def writeSumSquares():
    infile = input("enter infile name")
    outfile = input('enter outfile name')
    readfile = open(infile, 'r')
    writefile = open(outfile, 'w')
    for line in readfile:
        nums = line.split(',')
        toNumbers(nums)
        squareEach(nums)
        summation = sumList(nums)
        writefile.write('sum of squares = ' + str(summation) + "\n")


def starter():
    weight = float(input('enter players weight: '))
    numwins = int(input('enter the number of players wins: '))
    if 150 <= weight < 160 and numwins >= 5:
        print('the player should start')
    elif weight > 199 or numwins >= 20:
        print('the player should start')
    else:
        print('the player should not start')


def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def circleOverlap():
    win = GraphWin('circle', 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r1 = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, r1)
    c1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, r2)
    c2.draw(win)

    text = Text(Point(200, 300), 'the circles overlap')
    if math.sqrt((p3.getX() - p1.getX()) ** 2 + (p3.getY() - p1.getY()) ** 2) <= r1 + r2:
        text.draw(win)

    win.getMouse()
    win.close()



def main():
    # addTen([1, 2, 5])
    # squareEach([1, 2, 3])
    # sumList([1, 2, 3])
    # writeSumSquares()
    # starter()
    # leapYear(2004)
    # circleOverlap()

    pass


main()
