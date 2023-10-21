import turtle as t
class Paddle(t.Turtle):
   t.tracer(0)
   def __init__(self, position):
      super().__init__()
      self.color("white")
      self.penup()
      self.setpos(position)
      self.shape("square")
      self.turtlesize(5, 1)

   def go_up(self):
      self.goto(self.xcor(), self.ycor() + 20)
      # self.update()
   def go_down(self):
      self.goto(self.xcor(), self.ycor() - 20)