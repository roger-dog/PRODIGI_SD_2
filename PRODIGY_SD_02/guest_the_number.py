# 🎯 Prodigy InfoTech Task 02 – GUI Version
# Author: Roger (B.Tech Computer Engineering Intern)

import tkinter as tk
from ttkbootstrap import Style
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.style = Style("morph")  # Theme options: "flatly", "superhero", "cyborg"
        self.root.title("🎯 Guess the Number Game")

        self.target = random.randint(1, 100)
        self.attempts = 0

        # UI Elements
        self.label = tk.Label(root, text="Enter your guess (1-100):", font=("Segoe UI", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Segoe UI", 14))
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Guess", command=self.check_guess, font=("Segoe UI", 12))
        self.button.pack(pady=10)

        self.feedback = tk.Label(root, text="", font=("Segoe UI", 12), foreground="blue")
        self.feedback.pack(pady=5)

        self.counter = tk.Label(root, text="Attempts: 0", font=("Segoe UI", 10))
        self.counter.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback.config(text="⚠️ Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1
        self.counter.config(text=f"Attempts: {self.attempts}")

        if guess < self.target:
            self.feedback.config(text="📉 Too low!")
        elif guess > self.target:
            self.feedback.config(text="📈 Too high!")
        else:
            self.feedback.config(text=f"✅ Correct! You guessed it in {self.attempts} attempts.")
            self.button.config(state="disabled")

# Launch the GUI
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()