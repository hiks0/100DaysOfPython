from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, -620)
        self.setheading(90)
        self.pendown()
        for i in range(200):
            self.forward(10)
            self.color("black")
            self.forward(10)
            self.color("white")
