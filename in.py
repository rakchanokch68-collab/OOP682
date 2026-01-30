class Person:
    def __init__(self, name, age , pid):
        self.name = name
        self.age = age
        self.pid = pid
    def __str__(self):
        return f"Person[PID:{self.pid}, {self.name}, {self.age}]"

class Student(Person):
    def __init__(self, name, age, pid, student_id):
        super().__init__(name, age , pid)
        self.student_id = student_id
        
    def __str__(self):
        return f"Student[PID:{self.pid}, Name:{self.name}, Age:{self.age}, Student ID:{self.student_id}]"

class Staff(Person):
    def __init__(self, name, age, pid, staff_id):
        super().__init__(name, age , pid)
        self.staff_id = staff_id
    def __str__(self):
        return f"Staff[PID:{self.pid}, Name:{self.name}, Age:{self.age}, Staff ID:{self.staff_id}]"

def get_person_info(person):
    print(isinstance(person, Person))
    return f"Name: {person.name}, Age: {person.age}, PID: {person.pid}"


student1 = Student("Alice", 20, "P123", "S456")
staff1 = Staff("Bob", 35, "P789", "ST101")
print(f"Student Name: {student1.name}, Age: {student1.age}, PID: {student1.pid}, Student ID: {student1.student_id}")
print(f"Staff Name: {staff1.name}, Age: {staff1.age}, PID: {staff1.pid}, Staff ID: {staff1.staff_id}")



get_person_info(student1)
get_person_info(staff1)

#class employee:
#pass
#manager = employee()
#get_person_info(manager