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
    previous_balance = eval(input("previous net balance: "))
    payment = eval(input("payment amount: "))
    payment_day = eval(input("day payment received: "))
    average_daily_balance = ((previous_balance * days) - (payment * (days - payment_day))) / days
    monthly_interest = rate / 12 / 100 * average_daily_balance
    print(round(monthly_interest, 2))



#main()
