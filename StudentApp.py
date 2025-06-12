import tkinter as tk
from tkinter import messagebox
from record_manager_ import RecordManager
from student_class import Student

class StudentApp:
    def __init__(self, root):
        self.manager = RecordManager()
        self.root = root
        self.root.title("🎓 Student Records Management System")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        
        form_frame = tk.Frame(root, padx=10, pady=10)
        form_frame.pack(fill="x")
#
        tk.Label(form_frame, text="Student ID:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.id_entry = tk.Entry(form_frame, width=30)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Name:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.name_entry = tk.Entry(form_frame, width=30)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Grade:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.grade_entry = tk.Entry(form_frame, width=30)
        self.grade_entry.grid(row=2, column=1, padx=5, pady=5)

        
        btn_frame = tk.Frame(root, pady=10)
        btn_frame.pack()

        tk.Button(btn_frame, text="➕ Add", width=10, command=self.add_student).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="✏️ Update", width=10, command=self.update_student).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="🗑️ Delete", width=10, command=self.delete_student).grid(row=0, column=2, padx=5)

        
        self.listbox = tk.Listbox(root, width=65, height=12)
        self.listbox.pack(pady=10)
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
    
    def on_select(self, event):
        selected = self.listbox.curselection()
        if selected:
            student = self.manager.get_students()[selected[0]]
            self.id_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.grade_entry.delete(0, tk.END)

            self.id_entry.insert(0, student.student_id)
            self.name_entry.insert(0, student.name)
            self.grade_entry.insert(0, student.grade)

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for student in self.manager.get_students():
            self.listbox.insert(tk.END, str(student))


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root) 
    root.mainloop()
