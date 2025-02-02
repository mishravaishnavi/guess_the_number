import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.geometry("300x200")

        self.secret_number = random.randint(1, 100)
        self.attempts_left = 7

        self.label = tk.Label(root, text="Guess a number between 1 and 100!")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.attempts_label = tk.Label(root, text=f"Attempts left: {self.attempts_left}")
        self.attempts_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts_left -= 1

            if guess == self.secret_number:
                messagebox.showinfo("Congratulations!", f"You guessed the number {self.secret_number} correctly!")
                self.root.destroy()
            elif guess < self.secret_number:
                messagebox.showinfo("Too Low", "Try a higher number!")
            else:
                messagebox.showinfo("Too High", "Try a lower number!")

            self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")

            if self.attempts_left == 0:
                messagebox.showinfo("Game Over", f"You ran out of attempts! The number was {self.secret_number}.")
                self.root.destroy()

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number!")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()