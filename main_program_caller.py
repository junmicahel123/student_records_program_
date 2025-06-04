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