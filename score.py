from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 50, 'bold')


class Score(Turtle):
    def __init__(self, location):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        if location == "l":
            self.goto(-200, 220)
        elif location == "r":
            self.goto(200, 220)
        self.score_board()

    def score_board(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.score_board()

