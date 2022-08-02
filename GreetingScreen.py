from tkinter import (
    RIGHT,
    Tk,
    Frame, Label, Entry, Button,
    BOTH,
    RAISED
)

class GreetingScreen(Frame):
    def __init__(self):

        super().__init__()
        
        self.new_user_button = Button(self, text="New User")
        self.log_in_button = Button(self, text="Log In")

        self.name_label = Label(self, text="Name: ")
        self.password_label = Label(self, text="Password: ")

        self.name_entry = Entry(self, width=20)
        self.password_entry = Entry(self, width=20)
        
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1, columnspan=3)

        self.password_label.grid(row=1, column=0)
        self.password_entry.grid(row=1, column=1, columnspan=3)

        self.new_user_button.grid(row=2, column=0, columnspan=2)
        self.log_in_button.grid(row=2, column=2, columnspan=2)

