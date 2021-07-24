import time
from turtle import Screen
from paddle import Bars
from ball import Ball
from score_board import Score

scores = Score()
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
r_paddle = Bars(350, 0)
l_paddle = Bars(-350, 0)

balls = Ball()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
loop = True
while loop:
    time.sleep(balls.speed_move)
    screen.update()
    balls.move_ball()
    if balls.ycor() > 280 or balls.ycor() < -280:
        balls.bounce()

    if balls.distance(r_paddle) < 50 and balls.xcor() > 320 or balls.distance(l_paddle) < 50 and balls.xcor() < -320:
        balls.bounce_back()

    if balls.xcor() > 350:
        balls.reset_ball()
        scores.update_l_score()
    if balls.xcor() < -350:
        balls.reset_ball()
        scores.update_r_score()



screen.exitonclick()
