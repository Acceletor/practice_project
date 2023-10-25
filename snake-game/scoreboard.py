from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
with open("data.txt") as data:
    HIGH_SCORE = int(data.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_num = 0
        self.high_score = HIGH_SCORE
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score_num} HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score_num += 1
        self.update_scoreboard()

    def reset(self):
        if self.score_num > self.high_score:
            self.high_score = self.score_num
        self.score_num = 0
        self.update_scoreboard()
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg=f"Game over.", align=ALIGNMENT, font=FONT)