#
import os
from student_class import Student

class RecordManager:
    def __init__(self, filename="student_records.txt"):
        self.records = []
        self.filename = filename
        self.load_from_file()

    def add_student(self, students):
        self.records.append(students)
        self.save_to_file()
    
    def remove_student(self, index):
        if 0 <= index < len(self.records):
            del self.records[index]
            self.save_to_file()

    def update_student(self, index, students):
        if 0 <= index <len(self.records):
            self.records[index] = students
            self.save_to_file()

    def get_students(self):
        return self.records
    
    def save_to_file(self):
        with open(self.filename, "a") as f:
            for student in self.records:
                line = f"{student.student_id},{student_name},{student_grade}\n"
                f.write(line)

    def load_from_file(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    student = Student(parts[0], parts[1], parts[2])
                    self.records.append(student)
    