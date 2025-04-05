import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Number Guessing Game")
        self.geometry("400x300")
        self.configure(bg="#f0f0f0")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to the Number Guessing Game!", font=("Arial", 14), bg="#f0f0f0")
        self.label.pack(pady=10)

        self.instructions = tk.Label(self, text="I have selected a number between 1 and 100. Can you guess it?", font=("Arial", 12), bg="#f0f0f0")
        self.instructions.pack(pady=5)

        self.entry = tk.Entry(self, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(self, text="Submit Guess", font=("Arial", 12), command=self.check_guess, bg="#4CAF50", fg="white")
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 12), bg="#f0f0f0")
        self.result_label.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.result_label.config(text="Too low!")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high!")
            else:
                messagebox.showinfo("Congratulations!", f"You've guessed the number in {self.attempts} attempts.")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    app = NumberGuessingGame()
    app.mainloop()
