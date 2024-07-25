from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()  # To access objects & attributes in turtle class.

        # Setting up paddle qualities.
        self.turtlesize(stretch_len=5)
        self.tilt(90)
        self.color("white")
        self.speed(8)
        self.shape("square")
        self.penup()
        self.setposition(position)

    def up(self):
        new_y_cord = self.ycor() + 20
        self.goto(self.xcor(), new_y_cord)

    def down(self):
        # My brute force attempt: self.goto(350, -40)
        new_y_cord = self.ycor() - 20
        self.goto(self.xcor(), new_y_cord)
