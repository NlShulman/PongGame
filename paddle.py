from turtle import Turtle
MOVE_DISTANCE = 35
x_POSITION = 350


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.x_position = x_position

        self.setposition(self.x_position, 0)


    def move_up(self):
        y_pos = self.ycor()
        if y_pos <= 210:
            self.goto(self.x_position, y_pos + MOVE_DISTANCE)


    def move_down(self):
        y_pos = self.ycor()
        if y_pos >= - 210:
            self.goto(self.x_position, y_pos - MOVE_DISTANCE)


