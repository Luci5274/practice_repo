import datetime

class Habit:
    def __init__(self,habit_name,completions=None):
        self.habit_name =habit_name
        self.completions = completions if completions is not None else {}

habit_list = {}

    def add_habit(self, habit_name):
        if habit_name in self.habit_list:
            print(f'added {habit_name} to habit list')
