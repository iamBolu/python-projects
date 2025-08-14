from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x_loc,y_loc):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(x_loc,y_loc)

    def up(self):
        new_up = self.ycor() + 20
        self.goto(self.xcor(), new_up)

    def down(self):
        new_down = self.ycor() - 20
        self.goto(self.xcor(), new_down)