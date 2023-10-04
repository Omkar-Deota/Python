from turtle import Screen
from bar import Bar
from ball import Ball
import time
from score import Score
screen = Screen()
points=Score()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)
right_paddle = Bar((350,0))
left_paddle = Bar((-350,0))
ball = Ball()
screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, "d")
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #bounce by paddles
    if ball.distance(right_paddle)<50 and ball.xcor()>320 or ball.distance(left_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #ball misses the paddle
    if ball.xcor()>380:
        ball.reset_position()
        points.l_point()
    if ball.xcor()<-380:
        ball.reset_position()
        points.r_point()
screen.exitonclick()