#
class Student:
    def __init__(self, student_id, name, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def __str__(self):
        return f"{self.name} - {self.student_id} - {self.grade}"
    
    