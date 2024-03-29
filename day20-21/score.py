from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.goto(0, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align="center", font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER. final score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()
