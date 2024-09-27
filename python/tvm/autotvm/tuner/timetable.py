import time
from collections import defaultdict

class TimeTable():
    def __init__(self):
        self.temp = {}
        self.timetable = defaultdict(float)
        
    def start(self, key):
        if key in self.temp:
            raise ValueError(f"Key {key} already exists")
        self.temp[key] = time.time()
        
    def end(self, key):
        self.timetable[key] += time.time() - self.temp[key]
        del self.temp[key]
        
    def display(self):
        table = "\n"
        if self.temp:
            raise ValueError(f"Keys {self.temp.keys()} are still running")
        for key, value in self.timetable.items():
            table += f"{key}: {value}\n"
        print(table)