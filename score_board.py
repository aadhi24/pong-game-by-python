from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update_scores()



    def update_scores(self):
        self.clear()
        self.goto(-70, 250)
        self.write(self.l_score, align="center",font= ("Aral", 24, "normal"))
        self.goto(70, 250)
        self.write(self.r_score, align="center", font=("Aral", 24, "normal"))

    def update_r_score(self):
        self.r_score += 1
        self.update_scores()
    def update_l_score(self):
        self.l_score += 1
        self.update_scores()