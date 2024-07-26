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

    def print_day_num_row(self):
        for i in range (1, self.num_days + 1):
            print(i, end = ' ')
        print()

    def print_day_name_row(self):
        start_day = calendar.monthrange(self.year, self.month)[0]
        day_names = list(calendar.day_name)

        for i in range (0, self.num_days):
            print(day_names[(start_day + i) % 7], end = ' ')
        print()

    def print_table(self):
        self.print_day_num_row()
        self.print_day_name_row()
