from datetime import time
from shift import Shift

class ShiftFactory:
    @staticmethod
    def init_f():
        return Shift(
            "F",
            time(6,0),
            time(10,0),
            0
        )

    @staticmethod
    def init_f1():
        return Shift(
            "F1",
            time(7,0),
            time(14,0),
            30
        )

    @staticmethod
    def init_f2():
        return Shift(
            "F2",
            time(5,0),
            time(9,0),
            0
        )

    @staticmethod
    def init_f3():
        return Shift(
            "F3",
            time(5,0),
            time(10,0),
            0
        )


    @staticmethod
    def init_f4():
        return Shift(
            "F4",
            time(5,0),
            time(11,0),
            0
        )


    @staticmethod
    def init_f5():
        return Shift(
            "F5",
            time(5,0),
            time(12,0),
            30
        )

    @staticmethod
    def init_f6():
        return Shift(
            "F6",
            time(5,0),
            time(13,0),
            30
        )

    @staticmethod
    def init_f7():
        return Shift(
            "F7",
            time(5,0),
            time(14,0),
            30
        )
