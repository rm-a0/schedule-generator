#!/usr/bin/env python3
from schedule import Schedule
from employee import Employee

def main():
    schedule = Schedule(8, 2024)
    emp1 = Employee("Abcd", 23, "fulltime")
    schedule.print_table(emp1)

if __name__ == "__main__":
    main()
