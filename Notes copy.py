from tkinter import (
    ACTIVE, BOTH, DISABLED, END, LEFT, RAISED, SUNKEN, TOP,
    Frame, Label, Button, Text, Entry,
    Tk
)
from tkinter.font import NORMAL
from tkinter.messagebox import NO
from Note import Note


class Notes(Frame):

    def __init__(self):
        super().__init__()

        self.create_ui()

        self.counter = 1
        self.notes = set()
        self.active_note = None
    
    def create_ui(self):
        self.notes_list = Frame(self, background="grey87")
        self.notes_text = Frame(self)
        self.notes_buttons = Frame(self.notes_list)

        self.delete = Button(self.notes_buttons,
                             text="Удалить", command=self.delete_note)
        self.clone = Button(self.notes_buttons,
                            text="Дублировать", command=self.clone_note)
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
    
    def accept_name(self, entry, inpt):

            note = Note(self.notes_list, name=inpt.get())
            self.register_note(note)

            entry.destroy()

    
    def register_note(self, note):
        self.notes.add(note)
        note.pack(side="top")
        note.config(command=lambda: self.set_active_note(note))
    
    def set_active_note(self, new_active_note):

        if self.active_note != None:
            self.active_note.text = self.note_container.get("1.0", "end-1c")
            self.active_note.config(relief=RAISED)

        self.delete.config(state=NORMAL)
        self.clone.config(state=NORMAL)
        self.note_container.config(state=NORMAL)

        self.note_container.delete("1.0", END)
        self.note_container.insert("1.0", new_active_note.text)
        new_active_note.config(relief=SUNKEN)

        self.active_note = new_active_note

    def remove_active_note(self):
        self.delete.config(state=DISABLED)
        self.clone.config(state=DISABLED)
        self.note_container.delete("1.0", END)
        self.note_container.config(state=DISABLED)

        self.active_note = None

    
    def add_note(self):
        # self.counter += 1

        entry = Frame(self.notes_list)
        input_ = Entry(entry, width=15)
        button = Button(entry, text="Создать",
            command=lambda: self.accept_name(entry, input_)
        )

        input_.pack(side=LEFT)
        button.pack(side=LEFT)
        entry.pack(side=TOP)

    def delete_note(self):
        key = self.active_note
        self.notes.remove(key)
        key.destroy()

        self.remove_active_note()


    def clone_note(self):
        if self.active_note == None:
            pass
        else:
            new_note = Note(note=self.active_note)
            new_note.text = self.note_container.get("1.0", "end-1c")
            self.register_note(new_note)
            

        '''for key in self.notes:
            if key == self.active_note:
                name_copy = "Заметка " + str(self.counter) + "(копия)"
                note_copy = Button(self.notes_list, text=name_copy)
                note_copy.pack(side="top")
                self.notes[note_copy] = ""'''




if __name__ == "__main__":
    root = Tk()
    app = Notes()
    app.pack()
    root.mainloop()
