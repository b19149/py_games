import random
import turtle as t
class Ball(t.Turtle):
   def __init__(self):
      super().__init__()
      self.speed(1)
      self.shape("circle")
      self.penup()
      self.color("white")
      self.x_m = 10
      self.y_m = 10
      self.move_speed = 0.1
      
   def move(self):
      new_x = self.xcor() + self.x_m
      new_y = self.ycor() + self.y_m
      self.goto(new_x, new_y)
   
   def bounce_y(self):
      self.y_m *= -1
   def bounce_x(self):
      self.x_m *= -1
      self.move_speed *= 0.9

   def reset(self):
      self.goto(0, 0)
      self.bounce_x()
      self.move_speed = 0.1