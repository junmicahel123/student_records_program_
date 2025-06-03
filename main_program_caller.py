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
