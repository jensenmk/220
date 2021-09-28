"""
Name: Mark Jensen

Problem: Calculate traffic patterns on various roads

Certificate of Authenticity: I certify that this work is entirely my own
"""


def main():
    roads = eval(input("How many roads were surveyed? "))
    acc2 = 0
    for i in range(roads):
        days = eval(input("How many days was road " + str(i + 1) + " surveyed? "))
        acc = 0
        for j in range(days):
            num = eval(input("\tHow many cars traveled on day " + str(j + 1) + "? "))
            acc = num + acc
        daily_avg = acc / days
        print("Road " + str(i + 1) + " average vehicles per day: " + str(round(daily_avg, 2)))
        acc2 = acc + acc2
    tot_avg = acc2 / roads
    tot_cars = acc2

    print("Total number of vehicles traveled on all roads: " + str(tot_cars))
    print("Average number of vehicles per road: " + str(round(tot_avg, 2)))


if __name__ == "__main__":
    main()
