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


class StudentApplication:
    def __init__(self, root):
        self.root = RecordManager()
        self.root = root
        self.root.title = ("Student Records Management Office")
        