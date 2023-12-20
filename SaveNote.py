import pickle

class Notepad:
    def __init__(self, file_path="notepad.pkl"):
        self.notes = []
        self.file_path = file_path
        self.load_notes()

    def add_note(self, note_text):
        self.notes.append(note_text)
        self.save_notes()

    def display_notes(self):
        for i, note in enumerate(self.notes, 1):
            print(f"Note {i}: {note}")

    def save_notes(self):
        with open(self.file_path, 'wb') as file:
            pickle.dump(self.notes, file)

    def load_notes(self):
        try:
            with open(self.file_path, 'rb') as file:
                self.notes = pickle.load(file)
        except FileNotFoundError:
            self.save_notes()
