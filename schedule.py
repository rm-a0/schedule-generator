import calendar

class Schedule():
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.employees = []
        self.get_num_days()

    def append_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        employees.remove(employee)

    def get_num_days(self):
        self.num_days = calendar.monthrange(self.year, self.month)[1]

    def print_table(self):
        for i in range (1, self.num_days + 1):
            print(i, end = ' ')
        print()
