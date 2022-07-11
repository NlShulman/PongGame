from turtle import Turtle
import paddle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_step = 5
        self.y_step = 5
        self.delay_time = 0.04

    def ball_move(self):
        x_cor = self.xcor() + self.x_step
        y_cor = self.ycor() + self.y_step
        self.goto(x_cor, y_cor)

    def check_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_step = - self.y_step

    def check_paddle(self):
        self.x_step = - self.x_step
        self.increase_speed()

    def check_r_miss(self):
        if self.xcor() > 360:
            return True

    def check_l_miss(self):
        if self.xcor() < -360:
            return True

    def ball_reset(self):
        self.goto(0, 0)
        self.delay_time = 0.04
        self.x_step = - self.x_step

    def increase_speed(self):
        self.delay_time *= 0.9

