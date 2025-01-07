import json
import random
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class QuizApp:
    def __init__(self, root):
        self.root = root     # This root window will display the GUI components
        self.root.title("Quiz Game")     #Sets the title of the window.
        self.root.geometry("600x400")    
        self.questions = self.load_questions()
        random.shuffle(self.questions)     #Shuffles the order of the questions randomly.
        self.current_question_index = 0
        self.score = 0

        # Title Label
        self.title_label = ttk.Label(
            self.root, text="Quiz Game", font=("Helvetica", 20, "bold"), anchor="center"
        )
        self.title_label.pack(pady=20)

        # Question Label
        self.question_label = ttk.Label(
            self.root, text="", font=("Helvetica", 14), wraplength=500, anchor="center"
        )
        self.question_label.pack(pady=20)

        # Options Frame
        self.options_frame = ttk.Frame(self.root)   #Contains the buttons for the options.
        self.options_frame.pack(pady=20)

        # Buttons for Options
        self.option_buttons = []
        for i in range(4):
            button = ttk.Button(
                self.options_frame,
                text=f"Option {i+1}",
                command=lambda i=i: self.check_answer(i),
                style="primary.TButton",
            )
            button.pack(fill=X, pady=5)
            self.option_buttons.append(button)

        # Navigation Buttons
        self.navigation_frame = ttk.Frame(self.root)
        self.navigation_frame.pack(pady=20)
        self.next_button = ttk.Button(
            self.navigation_frame,
            text="Next Question",
            command=self.next_question,
            state=DISABLED,
            style="success.TButton",
        )
        self.next_button.pack(side=LEFT, padx=10)

        # Initialize the first question
        self.display_question()

    def load_questions(self):
        """Load questions from a JSON file."""
        try:
            with open("questions.json") as file:
                return json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "questions.json file not found.")
            self.root.destroy()
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON format in questions.json.")
            self.root.destroy()

    def display_question(self):
        """Display the current question and its options."""
        question_data = self.questions[self.current_question_index]
        self.question_label.config(text=question_data["question"])
        for idx, option in enumerate(question_data["options"]):
            self.option_buttons[idx].config(text=option, state=NORMAL)
        self.next_button.config(state=DISABLED)

    def check_answer(self, selected_index):
        """Check if the selected answer is correct."""
        question_data = self.questions[self.current_question_index]
        correct_answer = question_data["answer"]
        selected_answer = question_data["options"][selected_index]

        # Disable all buttons after an answer is selected
        for button in self.option_buttons:
            button.config(state=DISABLED)

        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "✅ That's correct!")
        else:
            messagebox.showerror(
                "Incorrect", f"❌ Incorrect! The correct answer is: {correct_answer}"
            )

        self.next_button.config(state=NORMAL)

    def next_question(self):
        """Move to the next question or end the quiz if completed."""
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        """Display the final score and end the quiz."""
        messagebox.showinfo(
            "Quiz Complete",
            f"You completed the quiz!\nYour score: {self.score}/{len(self.questions)}",
        )
        self.root.destroy()

if __name__ == "__main__":
    root = ttk.Window(themename="lumen")  # Using a ttkbootstrap theme
    app = QuizApp(root)
    root.mainloop()