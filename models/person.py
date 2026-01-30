

class Person:
    def __init__(self, name, age , pid):
        self.name = name
        self.age = age
        self.pid = pid
    def __str__(self):
        return f"Person[PID:{self.pid}, {self.name}, {self.age}]"