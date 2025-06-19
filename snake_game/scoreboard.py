from turtle import Turtle
from food import Food
ALIGMENT = "center"
FONT = ("Arial", 12, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.update_score()

    def update_score(self):
        self.write(f"Score={self.score}", False, ALIGMENT, FONT)
    def new_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_is_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, ALIGMENT, FONT)





