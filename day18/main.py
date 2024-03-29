import turtle
from turtle import Turtle, Screen
import colorgram
import random as rd

rgb_color = []
color = colorgram.extract('image.jpg', 10)
for color in color:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)
tim = Turtle()
turtle.colormode(255)
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range(10):
    for j in range(10):
        tim.dot(20, rd.choice(rgb_color))
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = Screen()
screen.exitonclick()
