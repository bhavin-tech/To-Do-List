import os
from datetime import datetime

class Note:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class ToDoList:
    def __init__(self):
        self.notes = []

    def add_note(self, title, description):
        new_note = Note(title, description)
        self.notes.append(new_note)
        print(f'Note "{title}" added to the list.')

    def view_notes(self):
        if not self.notes:
            print("No notes in the list.")
        else:
            print("To-Do List:")
            print(f"{'Sr. No.':<10}{'Title':<20}{'Description':<30}{'Date & Time':<20}")
            for idx, note in enumerate(self.notes, 1):
                print(f"{idx:<10}{note.title:<20}{note.description:<30}{note.datetime:<20}")

    def edit_note(self, note_number, new_title, new_description):
        if 0 < note_number <= len(self.notes):
            self.notes[note_number - 1].title = new_title
            self.notes[note_number - 1].description = new_description
            self.notes[note_number - 1].datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f'Note {note_number} edited.')
        else:
            print("Invalid note number.")

    def remove_note(self, note_number):
        if 0 < note_number <= len(self.notes):
            removed_note = self.notes.pop(note_number - 1)
            print(f'Note "{removed_note.title}" removed from the list.')
        else:
            print("Invalid note number.")

    def clear_notes(self):
        self.notes.clear()
        print("All notes cleared.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add note")
        print("2. View notes")
        print("3. Edit note")
        print("4. Remove note")
        print("5. Clear all notes")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter the title: ")
            description = input("Enter the description: ")
            todo_list.add_note(title, description)
        elif choice == '2':
            todo_list.view_notes()
        elif choice == '3':
            note_number = int(input("Enter the note number to edit: "))
            new_title = input("Enter the new title: ")
            new_description = input("Enter the new description: ")
            todo_list.edit_note(note_number, new_title, new_description)
        elif choice == '4':
            note_number = int(input("Enter the note number to remove: "))
            todo_list.remove_note(note_number)
        elif choice == '5':
            todo_list.clear_notes()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()