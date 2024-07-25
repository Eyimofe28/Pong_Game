from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_distance = 8
        self.y_distance = 8
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.setposition(0, 0)
        self.move_speed = 0.1

    def move(self):
        new_x_cord = self.xcor() + self.x_distance
        new_y_cord = self.ycor() + self.y_distance
        self.goto(new_x_cord, new_y_cord)

    def vertical_bounce(self):
        # This basically works by reversing the current direction of the Y-Axis,
        # i.e. if the ball reaches the tip-top, the y-cord is converted to negative to bring it down and vice versa.
        self.y_distance *= -1

    def horizontal_bounce(self):
        self.x_distance *= -1
        # Increases ball speed
        self.move_speed *= 0.8

    def reset_game(self):
        self.setposition(0, 0)
        self.horizontal_bounce()
        self.move_speed = 0.1
