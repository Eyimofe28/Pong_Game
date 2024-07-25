from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.left_count = 0
        self.right_count = 0
        self.scores()

    def scores(self):
        self.goto(-100, 200)
        self.write(arg=f"{self.left_count}", move=False, align='center', font=("Helvetica", 60, 'bold'))
        self.goto(100, 200)
        self.write(arg=f"{self.right_count}", move=False, align='center', font=("Helvetica", 60, 'bold'))

    def left_score_increase(self):
        self.left_count += 1
        self.clear()
        self.scores()

    def right_score_increase(self):
        self.right_count += 1
        self.clear()
        self.scores()

    def winner(self, x, y):
        self.goto(x, y)
        self.write(arg='You Win!🥳', move=False, align='center', font=("Helvetica", 30, 'italic'))

    def loser(self, x, y):
        self.goto(x, y)
        self.write(arg='You Lose😣', move=False, align='center', font=("Helvetica", 30, 'italic'))
