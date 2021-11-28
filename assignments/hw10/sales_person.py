"""
Mark Jensen
Problem: create a sales person class
Certificate of authenticity: I certify that this work is entirely my own
"""


class SalesPerson:
    """ 'SalesPerson' class created with (employee_id, name),
         assigns empty sales list and a total = '0'  """
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []
        self.total = 0

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        self.total = sum(self.sales)
        return self.total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        return sum(self.sales) >= quota

    def compare_to(self, other):
        if sum(self.sales) == sum(other.sales):
            return 0
        if sum(self.sales) > sum(other.sales):
            return 1
        if sum(self.sales) < sum(other.sales):
            return -1
        return "error"

    def __str__(self):
        return "{0}-{1}:{2}".format(self.employee_id, self.name, sum(self.sales))
