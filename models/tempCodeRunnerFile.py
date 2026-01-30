class Student(Person):
    def __init__(self, name, age, pid, student_id):
        super().__init__(name, age , pid)
        self.student_id = student_id
        
    def __str__(self):
        return f"Student[PID:{self.pid}, Name:{self.name}, Age:{self.age}, Student ID:{self.student_id}]"