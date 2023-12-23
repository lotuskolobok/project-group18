import os
from pathlib import Path
from rich.console import Console
from rich.table import Table
import pickle

class Notebook:
    def __init__(self):
        self.notes = []
        self.file_path = Path("notebook.bin")

    def add_note(self, note):
        self.notes.append(note)

    def get_notes(self):
        return self.notes

    def search_notes(self, query):
        return [note for note in self.notes if query in note.title or query in note.content or any(query in tag for tag in note.tags)]

    def change_note(self, note, new_title, new_content, new_tags):
        note.title = new_title
        note.content = new_content
        note.tags = new_tags

    def delete_note(self, note):
        self.notes.remove(note)

    def save(self):
        with open(self.file_path, "wb") as f:
            f.write(pickle.dumps(self.notes))

    def load(self):
        if self.file_path.exists():
            with open(self.file_path, "rb") as f:
                self.notes = pickle.load(f)
                


    def show_all(notebook):
        console = Console()

        table = Table(show_header=True, header_style="bold blue")
        table.add_column("№", justify="center", width=2)
        table.add_column("Name", justify="left", width=31)
        table.add_column("Note", justify="left", width=67)
        table.add_column("Tags", justify="left", width=26)
        table.add_column("Status", justify="left", width=11)

        counter = 1
        for info in notebook.get_notes():
            name = info.name.value
            if len(info.tags) == 1:
                tags = info.tags[0].value
            elif len(info.tags) > 1:
                tags_l = []
                for tag in [tag.value for tag in info.tags]:
                    tags_l.append(tag)
                tags = ", ".join(tags_l)
            tags = tags if len(tags) < 26 else tags[:23]+"..."
            note = info.note.value
            note = note if len(note) < 67 else note[:63]+"..."
            status = info.status.value

            table.add_row(
                str(counter),
                name,
                note,
                tags,
                status,
            )
            counter += 1

        console.print(table)
        
    # def show_note():
    #     name = input("Which note do you want to see? ")
    #     if name.lower() == "cancel":
    #         return "Showing has been canceled"
    #     if self.notes(name):
    #         return NOTES_BOOK.show_record(name)
    #     else:
    #         return "Nothing match"
        
def hello():
    return "How can I help you?"
def help():
    print(f'To start working with the assistant, write one of the commands[bold magenta].\nYou can use these commands[/bold magenta]\U0001F60A\n', "-"*90)
    print(f'[bold blue]add:[/bold blue]    Adds a note to the notebook.\n', '-'*90)
    print(f'[bold blue]search:[/bold blue]  Searches for notes in the notebook by the following fields: name / tag / status.\n', '-'*90)
    print(f'[bold blue]change:[/bold blue]  Changes the information in the note: name / note / tag / status.\n', '-'*90)
    print(f'[bold blue]shownote:[/bold blue]  Show note which the user want to see.\n', '-'*90)
    print(f'[bold blue]show:[/bold blue]    Show all notes.\n', '-'*90)
    print(f'[bold blue]del:[/bold blue]     Deleting a note, or deleting completed notes.\n', '-'*90)
    print(f'[bold blue]cancel:[/bold blue]  An undo command anywhere in the assistant.\n', '-'*90)
    print(f'[bold blue]good bye, close, exit:[/bold blue] Exit the program.\n', '-'*90)
    command = input("Press any key to return. ")
    if command.lower() == "cancel":
        return "Exit from the help menu. "
    else:
        main()
        
def end_work():
    return "Good bye"


COMMANDS = {"hello": hello,
            "help": help,
            "add": Notebook.add_note,
            "search": Notebook.search_notes,
            "change": Notebook.change_note,
            "show": Notebook.show_all,
            "shownote": Notebook.show_note,
            "del": Notebook.delete_note,
            "end_work": end_work}


def parser(command):
    if command.lower() == "hello":
        return "hello"
    if command.lower() in ["good bye", "close", "exit"]:
        return "end_work"
    if command.lower() == "help":
        return "help"
    if command.split()[0].lower() == "add":
        return "add"
    if command.split()[0].lower() == "search":
        return "search"
    if command.split()[0].lower() == "change":
        return "change"
    if command.split()[0].lower() == "show":
        return "show"
    if command.split()[0].lower() == "shownote":
        return "shownote"
    if command.split()[0].lower() == "del":
        return "del"
    else:
        return "wrong_command"


def main():
    print("Hello. If you need help, write 'help'")
    while True:
        user_command = input(">>> ")
        command = parser(user_command)
        if command == "end_work":
            print(COMMANDS["end_work"]())
            break
        if command == "hello":
            print(COMMANDS["hello"]())
            continue
        if command == "help":
            print(COMMANDS["help"]())
            continue
        if command == "add":
            print(COMMANDS["add"]())
            continue
        if command == "shownote":
            print(COMMANDS["shownote"]())
            continue
        if command == "show":
            COMMANDS["show"]()
            continue
        if command == "wrong_command":
            print("Wrong command")
            continue
        if command == "search":
            COMMANDS[command]()
            continue
        print(COMMANDS[command]())


if __name__ == "__main__":
    main()