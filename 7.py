class Note:
    def __init__(self, text, tags):
        self.text = text
        self.tags = tags

class PersonalAssistant:
    # Попередні методи класу залишаються незмінними

    def add_note_with_tags(self, text, tags):
        new_note = Note(text, tags)
        self.notes.append(new_note)
        print("Note added successfully!")

# Приклад використання:

assistant = PersonalAssistant()

assistant.add_note_with_tags("Meeting at 2 PM", ["work", "meeting"])
assistant.add_note_with_tags("Shopping list", ["personal", "groceries"])
assistant.add_note_with_tags("Project deadline", ["work", "deadline"])
