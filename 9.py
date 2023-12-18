class Notepad:
    def __init__(self):
        self.notes = []

    def add_note(self, text, tags):
        note = {"text": text, "tags": tags}
        self.notes.append(note)

    def add_tags_to_note(self, note_index, new_tags):
        if 0 <= note_index < len(self.notes):
            self.notes[note_index]["tags"].extend(new_tags)

# Використання:
notepad = Notepad()
notepad.add_note("Це моя перша нотатка", ["особисте", "плани"])

# Додавання тегів до існуючої нотатки
notepad.add_tags_to_note(0, ["важливо", "робота"])
