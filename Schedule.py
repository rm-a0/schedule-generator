import calendar

class Schedule():
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.employees = []
        get_num_days()

    def append_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        employees.remove(employee)

    def get_num_days(self):
        self.num_days = calendar.monthrange(year, month)[1]
