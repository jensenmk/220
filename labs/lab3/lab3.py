"""
Name: Mark Jensen
lab3.py

Certificate of authenticity: I certify that this work is entirely my own
"""


def average():
    acc = 0
    grades = eval(input("how many grades to average: "))
    for i in range(grades):
        score = eval(input("enter homework grade on HW " + str(i + 1) + " "))
        acc = acc + score
    average = acc / grades

    print(average)


def tip_jar():
    acc = 0
    for i in range(5):
        tip = eval(input("enter tip amount " + str(i + 1) + " "))
        acc = acc + tip

    print("the total tip amount is", acc)


def newton():
    x = eval(input("What number do you want to find the square root of? "))
    refine = eval(input("How many times would you like to refine the approximation? "))
    approx = x / 2
    for i in range(1, refine):
        approx = (approx + x / approx) / 2

    print(approx)


def sequence():
    ui = eval(input("number of terms in a series: "))
    for i in range(1, ui + 1):
        x = 1 + (i//2 * 2)
        print(x, end=" ")


def pi():
    acc = 1
    ui = eval(input("number of terms in a series: "))
    for i in range(0, ui + 1):
        num = 2 + (i // 2 * 2)
        denom = 1 + ((i+1) // 2 * 2)
        frac = num / denom
        acc = acc * frac
    print(acc * 2)




#average()
#tip_jar()
#newton()
#sequence()
#pi()