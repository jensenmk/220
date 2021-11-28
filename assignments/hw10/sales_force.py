"""
Mark Jensen
Problem: create a Salesforce class
Certificate of Authenticity: I certify that this work is entirely my own
"""

from sales_person import SalesPerson


# helper function to create an object in the SalesPerson class
def make_sales_person(employee_id, name):
    return SalesPerson(employee_id, name)


class SalesForce:
    """ 'SalesForce' class is a list that holds information on all of the 'SalesPerson' objects """
    def __init__(self):
        self.sales_people = []

    def add_data(self, filename):
        """ Open a file and read lines, assigns variables, creates a sales_person per line,
            enters sales then appends sales_person to self.sales_people """
        with open(filename, 'r') as infile:
            for line in infile:
                line = line[:-1]
                employee_id, name, sales = line.split(',')
                employee_id = int(employee_id)
                name = name[1:]
                sales = sales[1:].split(' ')
                sales_person = make_sales_person(employee_id, name)
                # float numbers in sale list and add them to the sales_person
                for i in sales:
                    sales_person.enter_sale(float(i))
                # add sales_person object to the sales_people list
                self.sales_people.append(sales_person)

    def quota_report(self, quota):
        """ 'quota_report' returns a list with employee information and a
             True or False for meeting user input quota"""
        quota_list = []
        for employee in self.sales_people:
            quota_list.append([employee.get_id(), employee.get_name(),
                               employee.total_sales(), employee.met_quota(quota)])
        return quota_list

    def top_seller(self):
        """ 'top_seller' returns a list of the top seller and multiples if there are ties"""
        top_seller_list = []
        self.sales_people.sort(key=SalesPerson.total_sales, reverse=True)
        i = 0
        top_seller_list.append(self.sales_people[0])
        while self.sales_people[i] == self.sales_people[i + 1]:
            top_seller_list.append(self.sales_people[i+1])
            i += 1
        return top_seller_list

    def individual_sales(self, employee_id):
        """ 'individual_sales' returns a sales person for a given employee_id if
            it exists in self.sales_people, otherwise returns None"""
        id_dict = {}
        for i in range(len(self.sales_people)):
            id_dict[self.sales_people[i].get_id()] = self.sales_people[i]
        if employee_id in id_dict:
            return id_dict.get(employee_id)
        return None
