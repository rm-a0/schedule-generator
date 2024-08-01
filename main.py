#!/usr/bin/env python3
from schedule import Schedule
from employee import Employee
from shift import Shift 

def main():
    schedule = Schedule(8, 2024, 4)
    f = Shift("F1", 5, 6, 0.5)
    emp1 = Employee("Abcd", 23, "fulltime")
    emp2 = Employee("Efgh", 23, "fulltime")
    emp3 = Employee("Ijkl", 23, "fulltime")
    emps = [emp1, emp2, emp3]
    schedule.print_table(emps)

if __name__ == "__main__":
    main()
