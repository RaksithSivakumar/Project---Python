import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")
        self.root.geometry("500x400")

        self.flashcards = {}
        self.current_flashcard = None

       
        self.card_frame = tk.Frame(root, bg="white", width=400, height=250, relief="raised", borderwidth=2)
        self.card_frame.pack(pady=20)

        self.question_label = tk.Label(self.card_frame, text="", font=("Arial", 18), bg="white", wraplength=350)
        self.question_label.pack(pady=10)

        self.answer_label = tk.Label(self.card_frame, text="", font=("Arial", 18), bg="white", wraplength=350)
        self.answer_label.pack(pady=10)

        self.controls_frame = tk.Frame(root)
        self.controls_frame.pack(pady=10)

        self.add_button = tk.Button(self.controls_frame, text="Add Flashcard", command=self.add_flashcard)
        self.add_button.grid(row=0, column=0, padx=10)

        self.edit_button = tk.Button(self.controls_frame, text="Edit Flashcard", command=self.edit_flashcard)
        self.edit_button.grid(row=0, column=1, padx=10)

        self.delete_button = tk.Button(self.controls_frame, text="Delete Flashcard", command=self.delete_flashcard)
        self.delete_button.grid(row=0, column=2, padx=10)

        self.next_button = tk.Button(self.controls_frame, text="Next Flashcard", command=self.next_flashcard)
        self.next_button.grid(row=1, column=0, padx=10, pady=10)

        self.show_answer_button = tk.Button(self.controls_frame, text="Show Answer", command=self.show_answer)
        self.show_answer_button.grid(row=1, column=1, padx=10, pady=10)

        self.mark_correct_button = tk.Button(self.controls_frame, text="Mark Correct", command=self.mark_correct)
        self.mark_correct_button.grid(row=1, column=2, padx=10, pady=10)

        self.stats_label = tk.Label(root, text="Correct: 0 | Incorrect: 0", font=("Arial", 14))
        self.stats_label.pack(pady=10)

        self.correct_count = 0
        self.incorrect_count = 0

    def add_flashcard(self):
        question = simpledialog.askstring("Add Flashcard", "Enter the question:")
        answer = simpledialog.askstring("Add Flashcard", "Enter the answer:")
        if question and answer:
            self.flashcards[question] = answer
            messagebox.showinfo("Flashcard Added", "Flashcard added successfully!")
        else:
            messagebox.showwarning("Input Error", "Both question and answer are required.")

    def edit_flashcard(self):
        if self.current_flashcard:
            question = self.current_flashcard
            new_question = simpledialog.askstring("Edit Flashcard", "Edit the question:", initialvalue=question)
            new_answer = simpledialog.askstring("Edit Flashcard", "Edit the answer:", initialvalue=self.flashcards[question])
            if new_question and new_answer:
                del self.flashcards[question]
                self.flashcards[new_question] = new_answer
                messagebox.showinfo("Flashcard Edited", "Flashcard edited successfully!")
            else:
                messagebox.showwarning("Input Error", "Both question and answer are required.")
        else:
            messagebox.showwarning("Selection Error", "No flashcard selected to edit.")

    def delete_flashcard(self):
        if self.current_flashcard:
            question = self.current_flashcard
            del self.flashcards[question]
            self.current_flashcard = None
            self.question_label.config(text="")
            self.answer_label.config(text="")
            messagebox.showinfo("Flashcard Deleted", "Flashcard deleted successfully!")
        else:
            messagebox.showwarning("Selection Error", "No flashcard selected to delete.")

    def next_flashcard(self):
        if self.flashcards:
            self.current_flashcard = random.choice(list(self.flashcards.keys()))
            self.question_label.config(text=self.current_flashcard)
            self.answer_label.config(text="")
        else:
            messagebox.showwarning("No Flashcards", "There are no flashcards to display.")

    def show_answer(self):
        if self.current_flashcard:
            answer = self.flashcards[self.current_flashcard]
            self.answer_label.config(text=answer)
        else:
            messagebox.showwarning("Selection Error", "No flashcard selected to show answer.")

    def mark_correct(self):
        if self.current_flashcard:
            self.correct_count += 1
            self.stats_label.config(text=f"Correct: {self.correct_count} | Incorrect: {self.incorrect_count}")
            self.next_flashcard()
        else:
            messagebox.showwarning("Selection Error", "No flashcard selected to mark correct.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
