import calendar

class Schedule():
    def __init__(self, month, year, cell_width):
        self.month = month
        self.year = year
        self.month_cell_width = len(calendar.month_name[month]) + 2
        self.cell_width = cell_width
        self.employees = []
        self.get_num_days()

    def append_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def get_num_days(self):
        self.num_days = calendar.monthrange(self.year, self.month)[1]

    def truncate_words(self, words, num_chars):
        return [word[:num_chars] for word in words]

    def print_cell(self, content, width, align):
        c_str = str(content)
        word_len = len(c_str)

        if align == "center":
            padding = (width - word_len) // 2
            print(' ' * padding + c_str + ' ' * (width - word_len - padding), end = '')

        elif align == "left":
            print(c_str + ' ' * (width - word_len), end = '')

        elif align == "right":
            print(' ' * (width - word_len) + c_str, end = '')

    def print_day_num_row(self):
        self.print_cell(calendar.month_name[self.month], self.month_cell_width, "center")
        for i in range (1, self.num_days + 1):
            self.print_cell(i, self.cell_width, "center")
        print()

    def print_day_name_row(self):
        start_day = calendar.monthrange(self.year, self.month)[0]
        day_names = self.truncate_words(list(calendar.day_name), 2)

        self.print_cell("", self.month_cell_width, "center")

        for i in range (0, self.num_days):
            self.print_cell(day_names[(start_day + i) % 7], self.cell_width, "center")
        print()

    def print_line_row(self):
        for i in range (0, self.num_days*self.cell_width + self.month_cell_width):
            self.print_cell("-", 1, "center")
        print()

    def print_employee_row(self, employees):
        for employee in employees:
            self.print_cell(employee.name, self.month_cell_width, "center")
            self.print_cell(employee.name, self.cell_width, "center")
            print()
        print()

    def print_table(self, employees):
        self.print_day_num_row()
        self.print_day_name_row()
        self.print_line_row()
        self.print_employee_row(employees)
