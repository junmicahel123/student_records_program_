#
#
# Record manager
    # ADD
    # REMOVE    
    # UPDATE
    # SEARCH
    #
# (ILL TRY ADDING PHOTOS OF STUDENT)

import tkinter as tk
from tkinter import messagebox
from record_manager_ import RecordManager
from student_class import Student

class StudentApplication:
    def __init__(self, root):
        self.manager = RecordManager()
        self.root = root
        self.root.title = ("Student Records Management Office")


        self.id_entry = tk.Entry(root)
        self.name_entry = tk.Entry(root)
        self.grade_entry = tk.Entry(root)

        tk.Label(root, text="Student ID").grid(rows=0, column=0)
        self.id_entry.grid(row=0, column=1)
        tk.Label(root, text="Name").grid(row=1, column=0)
        self.name_entry.grid(row=1 , column=1)
        tk.Label(root, text="Grade").grid(row=2, column=0)
        self.grade_entry.grid(row=2, column=1)

        tk.Button(root, text="Add", command=self.add_student).grid(row=3, column=0)
        tk.Button(root, text="Update", command=self.update_student).grid(row=3, column=1)
        tk.Button(root, text="Delete", command=self.delete_student).grid(row=3, column=2)

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.grid(row=4, column=0, columnspan=3)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)

    def add_student(self):
        student = Student(self.id_entry.get(), self.name_entry.get(), self.grade_entry.get())
        self.manager.add_student(student)
        self.refresh_listbox()

    def delete_student(self):
        selected = self.listbox.curselection()
        if selected:
            self.manager.delete_student(selected[0])
            self.refresh_listbox()

    def update_student(self):
        selected = self.listbox.curselection()
        if selected:
            student = Student(self.id_entry.get(), self.name_entry.get(), self.grade_entry.get())
            self.manager.update_student(selected[0], student)
            self.refresh_listbox()
    
    def on_selected(self, event):
        selected = self.listbox.curselection()
        if selected:
            student = self.manager.records[selected[0]]
            self.id_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.grade_entry.delete(0, tk.END)

            self.id_entry.insert(0, student.student_id)
            self.name_entry.insert(0, student.name)
            self.grade_entry.insert(0, student.grade)

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for student in self.manager.get_all_students():
            self.listbox.insert(tk.END, str(student))

    
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApplication(root) 
    root.mainloop()