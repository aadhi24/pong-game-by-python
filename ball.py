from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.speed_move = 0.1
    def move_ball(self):
        x = self.xcor()+self.x_move
        y = self.ycor()+self.y_move
        self.goto(x, y)

    def bounce(self):
        self.y_move *= -1


    def bounce_back(self):
        self.x_move *= -1
        self.speed_move*= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_back()
        self.speed_move = 0.1






