import time
import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard as Score
scr = t.Screen()
scr.title("pong")
scr.bgcolor("black")
scr.setup(width = 800, height = 600)
scr.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-390, 0))
ball = Ball()
score = Score()
scr.listen()
scr.onkeypress(r_paddle.go_up , "Up")
scr.onkeypress(r_paddle.go_down , "Down")
scr.onkeypress(l_paddle.go_up , "w")
scr.onkeypress(l_paddle.go_down , "s")

game_on = True
while game_on:
   time.sleep(ball.move_speed)
   scr.update()
   ball.move()
   if ball.ycor() > 280 or ball.ycor() < -280:
      ball.bounce_y()
   if ball.distance(r_paddle) < 50  and ball.xcor() > 360 or ball.distance(l_paddle) < 50 and ball.xcor() < -370:
      ball.bounce_x()
   if ball.xcor() > 380:
      score.increase_l_score()
      ball.reset()
   if ball.xcor() < -380:
      score.increase_r_score()
      ball.reset()
   score.Print_scoreboard()
   
scr.exitonclick()
