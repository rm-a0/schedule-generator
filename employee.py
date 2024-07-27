class Employee():
    def __init__(self, name, age, contract_type):
        self.name = name
        self.age = age
        self.contract_type = contract_type
        self.shift_pref = None
        self.min_hpm = None
        self.max_hpm = None

    def change_shift_pref(self, new_shift_pref):
        self.shift_pref = new_shift_pref

    def change_min_hpm(self, new_min_hpm):
        self.min_hpm = new_min_hpm

    def change_max_hpm(self, new_max_hpm):
        self.max_hpm = new_max_hpm

