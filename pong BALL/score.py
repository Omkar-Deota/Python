from turtle import Turtle, Screen

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_point()
    def update_point(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align="center", font=("Courier,", 30, "normal"))
        self.goto(100, 220)
        self.write(self.r_score, align="center", font=("Courier,", 30, "normal"))

    def l_point(self):
        self.l_score+=1
        self.update_point()
    def r_point(self):
        self.r_score+=1
        self.update_point()