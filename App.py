from tkinter import Tk, BOTH
from GreetingScreen import GreetingScreen
from Notes import Notes


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("NoteApp")

        self.hello_screen = GreetingScreen()

        self.hello_screen.pack(fill=BOTH, expand=True)