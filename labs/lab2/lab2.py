"""
Name: <Mark Jensen>
lab2.py


"""


def sum_of_threes():
    upper_bound = eval(input("enter upper bound: "))
    acc = 0
    for x in range(0,upper_bound + 1,3):
        acc = acc + x
    print(acc)


def multiplication_table():
    for h in range(1,11):
        for l in range(1,11):
            print(l * h,end=" ")
        print()


def triangle_area():
    import math
    a = eval(input("a: "))
    b = eval(input("b: "))
    c = eval(input("c: "))
    s = (a+b+c)/2
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("area = ", A)


def sumSquares():
    start = eval(input("start: "))
    end = eval(input("end: "))
    acc = 0
    for x in range(start, end + 1):
        acc = acc + (x * x)
    print(acc)


def power():
    base = eval(input("base: "))
    exp = eval(input("exponent: "))
    acc = 1
    for x in range(exp):
        acc = acc * base
    print(acc)



sum_of_threes()
multiplication_table()
triangle_area()
sumSquares()
power()
