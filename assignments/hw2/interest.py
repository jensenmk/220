"""
name: <Mark Jensen>
interest.py

Problem: calculate monthly interest payment of a credit card

Certificate of Authenticity:
I certify that this work is entirely my own
"""

def main():
    rate = eval(input("annual interest rate: "))
    days = eval(input("number of days in billing cycle: "))
    previousBalance = eval(input("previous net balance: "))
    payment = eval(input("payment amount: "))
    paymentDay = eval(input("day payment received: "))
    average_daily_balance = ((previousBalance * days) - (payment * (days - paymentDay))) / days
    monthlyinterest = rate / 12 / 100 * average_daily_balance
    print("monthly interest: $", round(monthlyinterest, 2))

main()
