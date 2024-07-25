import turtle as t
from pong_paddle import Paddle
from pong_ball import Ball
from pong_scoreboard import ScoreBoard
import time

# Setting up the game environment.
screen = t.Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.tracer(0)
screen.title("PONG GAME")

# Creating the paddles.
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

# Creating the ball.
pong_ball = Ball()

# Creating Score Board.
score_board = ScoreBoard()

# Creating a line in the middle of the board.
line = t.Turtle()
line.color("white")
line.hideturtle()
line.pensize(7)
line.penup()
line.goto(0, -300)
line.setheading(90)

for i in range(0, 600):
    line.pendown()
    line.forward(25)
    line.penup()
    line.forward(20)

# Letting the paddle listen for movements.
screen.listen()

# Moving the right paddle with up and down arrows on keyboard.
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)

# Moving the left paddle up and down with w and s keys respectively on keyboard.
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

game_on = True

while game_on:
    screen.update()
    time.sleep(pong_ball.move_speed)  # Increasing the ball's speed when it collides with a paddle.
    pong_ball.move()

    # Detecting collision with walls.
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.vertical_bounce()

    # Detecting collision with paddles.
    if ((pong_ball.distance(right_paddle) < 50 and pong_ball.xcor() > 330) or
            (pong_ball.distance(left_paddle) < 50 and pong_ball.xcor() < -330)):
        # The determining factor for the first condition is 50 because the ball and
        # paddle centers are actually what determines the collision. This will allow
        # allowance for when this condition isn't met.
        pong_ball.horizontal_bounce()

    # Detecting when ball goes out off bounds on the right side.
    if pong_ball.xcor() > 380:
        pong_ball.reset_game()
        score_board.left_score_increase()

    # Detecting when ball goes out off bounds on the left side.
    if pong_ball.xcor() < -380:
        pong_ball.reset_game()
        score_board.right_score_increase()

    # Detecting if one of the  players has reached a certain score.
    if score_board.left_count == 7:
        pong_ball.clear()
        score_board.winner(-150, 50)
        score_board.loser(150, 50)
        game_on = False

    elif score_board.right_count == 7:
        pong_ball.clear()
        score_board.winner(150, 50)
        score_board.loser(-150, 50)
        game_on = False

screen.exitonclick()
