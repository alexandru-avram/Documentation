from turtle import Turtle
from tkinter import messagebox
score_alignment = "center"
score_font = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 450)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=score_alignment, font=score_font)

    def inscrease_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.clear()
        messagebox.showinfo("GAME OVER", f"Your final score is {self.score}")