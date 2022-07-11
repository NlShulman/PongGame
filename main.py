import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)

r_score = Score("r")
l_score = Score("l")

ball = Ball()

screen.listen()


screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(ball.delay_time)
    screen.update()
    ball.ball_move()
    ball.check_wall()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.check_paddle()

    if ball.check_r_miss():
        ball.ball_reset()
        l_score.update_score()

    if ball.check_l_miss():
        ball.ball_reset()
        r_score.update_score()



screen.exitonclick()

