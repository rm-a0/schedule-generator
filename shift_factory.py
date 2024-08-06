from datetime import time
from shift import Shift

class ShiftFactory:
    @staticmethod
    def init_f1():
        return Shift(
            "F1",
            time(7,0),
            time(14,0),
            30
        )
