import datetime

class Habit:
    def __init__(self,habit_name,completions=None):
        self.habit_name =habit_name
        self.completions = completions if completions is not None else {}