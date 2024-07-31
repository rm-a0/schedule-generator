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
        self.print_cell(calendar.month_name[self.month], len(calendar.month_name[self.month]) + 2, "center")
        for i in range (1, self.num_days + 1):
            self.print_cell(i, 4, "center")
        print()

    def print_day_name_row(self):
        start_day = calendar.monthrange(self.year, self.month)[0]
        day_names = self.truncate_words(list(calendar.day_name), 2)

        self.print_cell("", len(calendar.month_name[self.month]) + 2, "center")

        for i in range (0, self.num_days):
            self.print_cell(day_names[(start_day + i) % 7], 4, "center")
        print()

    def print_line_row(self):
        for i in range (0, self.num_days*4 + len(calendar.month_name[self.month]) + 2):
            self.print_cell("-", 1, "center")
        print()

    def print_employee_row(self, employee):
        self.print_cell(employee.name, len(employee.name), "center")

    def print_table(self, employee):
        self.print_day_num_row()
        self.print_day_name_row()
        self.print_line_row()
        self.print_employee_row(employee)
