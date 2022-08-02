from tkinter import (
    BOTH, Frame, Label, Button, Text,
    Tk
)


class Notes(Frame):

    def __init__(self):
        super().__init__()

        self.counter = 1

        self.notes_list = Frame(self, background="grey87")
        self.notes_text = Frame(self)
        self.notes_buttons = Frame(self.notes_list)

        self.delete = Button(self.notes_buttons,
                             text="Удалить", command=self.delete_note)
        self.clone = Button(self.notes_buttons,
                            text="Дублировать", command=self.clone)
        self.add = Button(self.notes_buttons, text="Добавить",
                          command=self.add_note)

        self.note_container = Text(self.notes_text)

        self.grid_rowconfigure(0, minsize=400, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=300)
        self.grid_columnconfigure(1, weight=5, minsize=300)

        self.notes_list.grid(row=0, column=0, sticky="nswe")
        self.notes_text.grid(row=0, column=1, sticky="nswe")
        self.notes_buttons.pack(side="bottom")

        self.delete.pack(side="left")
        self.clone.pack(side="left")
        self.add.pack(side="left")
        self.note_container.pack(fill=BOTH, expand=True)

        self.notes = {}

        self.active_note = None

    def delete_note(self):
        self.k = list(self.notes)
        try:
            for key in self.notes:
                if key == self.active_note:
                    key.destroy()
                    del self.notes[key]
                    self.k.remove(key)
                    self.active_note = self.k[0]
        except:
            pass

    def add_note(self):
        self.name = "Заметка " + str(self.counter)
        self.counter += 1
        self.note = Button(self.notes_list, text=self.name)
        self.note.pack(side="top")
        self.notes[self.note] = ""
        self.k = list(self.notes)

        if len(self.notes) == 1:
            self.active_note = self.k[0]

    def clone(self):
        try:
            for key in self.notes:
                if key == self.note:
                    self.name_copy = "Заметка " + \
                        str(self.counter-1) + "(копия)"
                    self.note_copy = Button(
                        self.notes_list, text=self.name_copy)
                    self.note_copy.pack(side="top")
                    self.notes[self.note_copy] = self.notes[self.active_note]
        except:
            pass



if __name__ == "__main__":
    root = Tk()
    app = Notes()
    app.pack()
    root.mainloop()
