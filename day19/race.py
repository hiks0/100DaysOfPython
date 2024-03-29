import random
from turtle import Turtle, Screen

race_on = False
screen = Screen()
screen.setup(height=400, width=500)
user_guess = screen.textinput(title="Make your bet", prompt="Which turtle will win the race: ")
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
y_pos = [-70, -40, -10, 20, 50, 80]
turtle_list = []
for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(-230, y_pos[turtle])
    turtle_list.append(new_turtle)

if user_guess:
    race_on = True

while race_on:
    for turtle in turtle_list:
        if turtle.xcor()>230:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_guess:
                print("You won")
            else:
                print(f"You lost, the winning color was {winner}")
        distance = random.randint(0, 10)
        turtle.forward(distance)
screen.exitonclick()


