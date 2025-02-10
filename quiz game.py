import tkinter as tk
from tkinter import messagebox
import random

questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Jupiter", "Saturn", "Venus"], "answer": "Mars"},
    {"question": "Who wrote 'Hamlet'?", "options": ["Shakespeare", "Hemingway", "Austen", "Dickens"], "answer": "Shakespeare"},
    {"question": "What is the largest ocean?", "options": ["Pacific", "Atlantic", "Indian", "Arctic"], "answer": "Pacific"},
]

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x500")
        
        self.time_left = 10
        self.current_question = None
        
        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=20)
        
        self.buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", width=20, font=("Arial", 12), command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)
        
        self.timer_label = tk.Label(root, text=f"Time left: {self.time_left}s", font=("Arial", 14))
        self.timer_label.place(x=400, y=20)
        
        self.load_question()
        self.update_timer()
        
    def load_question(self):
        self.time_left = 10
        self.current_question = random.choice(questions)
        questions.remove(self.current_question)
        self.question_label.config(text=self.current_question["question"])
        
        options = self.current_question["options"]
        random.shuffle(options)
        for i, option in enumerate(options):
            self.buttons[i].config(text=option)
    def check_answer(self, index):
        selected_answer = self.buttons[index].cget("text")
        if selected_answer == self.current_question["answer"]:
            messagebox.showinfo("Correct!", "You got it right!")
        else:
            messagebox.showinfo("Wrong!", "Better luck next time.")
            root.destroy()
        if len(questions) == 0:
            messagebox.showinfo("DONE!","YOU WON, CONGRATS!")
            root.destroy()
        self.load_question()
        
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time's up!", "Moving to the next question.")
            self.load_question()
            self.update_timer()
        
if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()
