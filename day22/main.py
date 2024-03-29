from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
from line import Line

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0), "blue")
l_paddle = Paddle((-350, 0), "red")
ball = Ball()
score = Score()
line = Line()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_on = True


while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 70 and ball.xcor() > 320 or ball.distance(l_paddle) < 70 and ball.xcor() < -320:
        ball.bounce_x()

    #detect when paddle misses
    if ball.xcor() > 350:
        ball.reset_pos()
        score.l_point()

    if ball.xcor() < -350:
        ball.reset_pos()
        score.r_point()


screen.exitonclick()
