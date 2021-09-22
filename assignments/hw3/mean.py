"""
Name: Mark Jensen
mean.py

Problem: calculate the root mean square, harmonic mean and geometric mean of a given set of numbers

Certificate of Authenticity: I certify that this work is entirely my own
"""

import math


def main():
    hmc_acc = 0  # hmc_acc = 0
    rms_acc = 0  # rms_acc = 0
    geo_acc = 1  # geo_acc = 1
    u_i = int(input("how many variables to average: "))  # ask for "n" number of numbers
    for i in range(u_i):  # range loop eval "number" + str(i+1) + " "
        var = float(input("enter variable " + str(i + 1) + " "))
        rms_acc = rms_acc + var ** 2  # rms_acc = i**2 + acc
        hmc_acc = hmc_acc + 1 / var  # hmc_acc = hmc_acc + 1/i
        geo_acc = geo_acc * var  # geo_acc = geo_acc * 1

    rms_average = math.sqrt(rms_acc/u_i)  # rms_average = math.sqrt(rms_acc/n)
    harmonic_mean = u_i / hmc_acc  # harmonic_mean = n/hmc_acc
    geo_mean = geo_acc ** (1 / u_i)  # geo_mean = geo_acc ** (1/n)
    print(round(rms_average, 3))  # output rms, harmonic mean, and geo mean
    print(round(harmonic_mean, 3))
    print(round(geo_mean, 3))


if __name__ == '__main__':
    main()
