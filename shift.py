from datetime import time

class Shift():
    def __init__(self, name, start, end, break_duration):
        self.name = name
        self.start = start
        self.end = end
        self.break_duration = break_duration

    def calc_duration(self):
        start_min = self.start.hour * 60 + self.start.minute
        end_min = self.end.hour * 60 + self.end.minute

        if end_min < start_min:
            end_min += 24 * 60

        total_min = end_min - start_min

        hrs = total_min // 60
        mins = total_min % 60

        return hrs, mins

    def calc_pay(self, hourly_wage):
        hrs, mins = self.calc_duration()

        total_mins = hrs * 60 + mins - self.duration

        work_hrs = total_mins // 60
        work_mins = total_mins % 60

        total_work_hrs = work_hrs + work_mins / 60.0
        total_pay = total_work_hrs * hourl_wage

        return total_pay
