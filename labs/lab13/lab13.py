"""
Name: Mark Jensen
lab13.py
"""


def main():
    print(is_in_binary(6, [1, 2, 3, 4, 6, 7, 8]))
    values = [4,3,2,5,1]
    selection_sort(values)
    print(values)
    star_find("signals.txt")
    pass


def is_in_binary(var, nums):
    i = 0
    j = len(nums)
    while i <= j:
        mid = (i + j) // 2
        mid_value = nums[mid]
        if mid_value > var:
            j = mid - 1
        if mid_value < var:
            i = mid + 1
        if mid_value == var:
            return True
    return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i + 1, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


def rect_sort(rects):
    dict = {}
    areas = []
    for rect in rects:
        dict[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rects[i] = dict[areas[i]]


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX - p2.getX)
    dy = abs(p1.getY - p2.getY)
    return dx * dy


def star_find(filename):
    file = open(filename, 'r')
    signals = file.read().split()
    found = []
    signal_list = []
    for signal in signals:
        signal = int(signal)
        signal_list.append(signal)
    count = 0
    for i in signal_list:
        if 4000 <= i <= 5000:
            found.append(i)
        if len(found) >= 5:
            break
        count += 1
    print(len(found))
    print(found)
    if len(found) < 5:
        print("we didnt find 5 signals")
    else:
        print(count)


main()
