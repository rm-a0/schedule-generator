class Employee():
    def __init__(self, name, age, contract_type):
        self.name = name
        self.age = age
        self.contract_type = contract_type
        self.shift_pref = None
        self.hours_per_month = None

    def change_shift_pref(self, new_shift_pref):
        self.shift_pref = new_shift_pref

    def change_hpm(self, new_hpm):
        self.hours_per_month = new_hpm

