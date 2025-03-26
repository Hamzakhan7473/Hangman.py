import tkinter as tk
from tkinter import messagebox
import random

WORDS = ["python", "hangman", "modular", "developer"]

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word = random.choice(WORDS)
        self.display = ["_"] * len(self.word)
        self.guessed = []
        self.attempts = 6

        self.canvas = tk.Canvas(root, width=200, height=250)
        self.canvas.pack()
        self.draw_gallows()

        self.label = tk.Label(root, text=" ".join(self.display), font=("Courier", 24))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Courier", 16))
        self.entry.pack()

        self.button = tk.Button(root, text="Guess", command=self.make_guess)
        self.button.pack(pady=10)

        self.status = tk.Label(root, text=f"Attempts Left: {self.attempts}", font=("Courier", 14))
        self.status.pack()

    def draw_gallows(self):
        self.canvas.create_line(20, 230, 180, 230, width=4)  # base
        self.canvas.create_line(50, 230, 50, 20, width=4)    # pole
        self.canvas.create_line(50, 20, 130, 20, width=4)    # top bar
        self.canvas.create_line(130, 20, 130, 50, width=4)   # rope

    def draw_hangman_stage(self):
        stage = 6 - self.attempts
        if stage == 1:
            self.canvas.create_oval(110, 50, 150, 90, width=2)  # head
        elif stage == 2:
            self.canvas.create_line(130, 90, 130, 150, width=2)  # body
        elif stage == 3:
            self.canvas.create_line(130, 100, 110, 130, width=2)  # left arm
        elif stage == 4:
            self.canvas.create_line(130, 100, 150, 130, width=2)  # right arm
        elif stage == 5:
            self.canvas.create_line(130, 150, 110, 190, width=2)  # left leg
        elif stage == 6:
            self.canvas.create_line(130, 150, 150, 190, width=2)  # right leg

    def make_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not guess.isalpha() or len(guess) != 1 or guess in self.guessed:
            messagebox.showinfo("Invalid", "Enter a valid single new letter.")
            return

        self.guessed.append(guess)

        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.display[i] = guess
            self.label.config(text=" ".join(self.display))
        else:
            self.attempts -= 1
            self.draw_hangman_stage()
            self.status.config(text=f"Attempts Left: {self.attempts}")

        if "_" not in self.display:
            messagebox.showinfo("Victory", "🎉 You guessed it right!")
            self.root.quit()

        elif self.attempts == 0:
            messagebox.showinfo("Defeat", f"😵 Out of attempts! Word was: {self.word}")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGUI(root)
    root.mainloop()
