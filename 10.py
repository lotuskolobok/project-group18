class Notepad:
    def __init__(self):
        self.notes = []

    def add_note(self, text, tags):
        note = {"text": text, "tags": tags}
        self.notes.append(note)

    def search_notes_by_tag(self, tag):
        matching_notes = [note for note in self.notes if tag in note["tags"]]
        return matching_notes

    def sort_notes_by_tag(self, tag):
        sorted_notes = sorted(self.notes, key=lambda x: tag in x["tags"])
        return sorted_notes

# Використання:
notepad = Notepad()
notepad.add_note("Це моя перша нотатка", ["особисте", "плани"])
notepad.add_note("Зустріч з другом", ["особисте", "плани", "подорож"])
notepad.add_note("Проект для роботи", ["робота", "плани"])

# Пошук нотаток за тегом
matching_notes = notepad.search_notes_by_tag("плани")
print("Нотатки з тегом 'плани':", matching_notes)

# Сортування нотаток за тегом
sorted_notes = notepad.sort_notes_by_tag("особисте")
print("Нотатки відсортовані за тегом 'особисте':", sorted_notes)
