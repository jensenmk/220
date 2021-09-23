"""
Name: Mark Jensen

Problem: Calculate traffic patterns on various roads

Certificate of Authenticity: I certify that this work is entirely my own
"""


def main():
    r_i = eval(input("How many roads were surveyed? "))
    acc_2 = 0
    for i in range(0, r_i):
        d_i = eval(input("how many days was road " + str(i + 1) + " " + "surveyed? "))
        acc = 0
        for y_i in range(0, d_i):
            num = eval(input("How many cars traveled on day " + str(y_i + 1) + "? "))
            acc = acc + num
        acc_2 = acc + acc_2
        d_1avg = acc / d_i
        print("road " + str(i) + " " + "average " + str(round(d_1avg, 2)))

    t_avr = acc_2 / r_i
    print("Total number of vehicles traveled on all roads: " + str(acc_2))
    print(("Average number of vehicles per road: " + str(round(t_avr, 2))))


if __name__ == "__main__":
    main()
