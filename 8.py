class Note:
    def __init__(self, text, tags):
        self.text = text
        self.tags = tags

class PersonalAssistant:
    # Попередні методи класу залишаються незмінними

    def search_notes_by_tag(self, tag):
        matching_notes = [note for note in self.notes if tag.lower() in note.tags]
        return matching_notes

    def sort_notes_by_tags(self):
        sorted_notes = sorted(self.notes, key=lambda note: note.tags)
        return sorted_notes

# Приклад використання:

assistant = PersonalAssistant()

note1 = Note("Meeting at 2 PM", ["work", "meeting"])
assistant.add_note(note1)

note2 = Note("Shopping list", ["personal", "groceries"])
assistant.add_note(note2)

note3 = Note("Project deadline", ["work", "deadline"])
assistant.add_note(note3)

# Пошук нотаток за тегом
searched_notes = assistant.search_notes_by_tag("work")
for note in searched_notes:
    print(f"Note: {note.text}, Tags: {note.tags}")

# Сортування нотаток за тегами
sorted_notes = assistant.sort_notes_by_tags()
for note in sorted_notes:
    print(f"Note: {note.text}, Tags: {note.tags}")
