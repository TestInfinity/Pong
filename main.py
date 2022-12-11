import random
import time
import turtle
from turtle import Turtle
import copy

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
player_score = 0
opponent_score = 0


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, 0)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 2
        self.dy = 2


# Player
player_paddle = Paddle(-350)

# Opponent
opponent_paddle = Paddle(350)

# Ball
ball = Ball()

# Pen
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Player: 0  Opponent: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_up(paddle):
    y = paddle.ycor()
    if y < 290:
        y += 10
        paddle.sety(y)


def paddle_down(paddle):
    y = paddle.ycor()
    if y > -290:
        y -= 10
        paddle.sety(y)


def opponent_decession():
    if ball.dx > 0:

        if abs(player_paddle.ycor() - ball.ycor()) > 30:
            if ball.ycor() > opponent_paddle.ycor():
                paddle_up(opponent_paddle)
            elif ball.ycor() < opponent_paddle.ycor():
                paddle_down(opponent_paddle)



# Keyboard bindings
wn.listen()
wn.onkeypress(lambda: paddle_up(player_paddle), "Up")
wn.onkeypress(lambda: paddle_down(player_paddle), "Down")

# Main game loop
try:
    while True:

        wn.update()
        time.sleep(0.009)

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking

        # Top and bottom
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Left and right
        if ball.xcor() > 350:
            player_score += 1
            scoreboard.clear()
            scoreboard.write(f"Player: {player_score}  Opponent: {opponent_score}", align="center",
                             font=("Courier", 24))
            ball.goto(0, 0)
            ball.dx *= -1

        elif ball.xcor() < -350:
            opponent_score += 1
            scoreboard.clear()
            scoreboard.write(f"Player: {player_score}  Opponent: {opponent_score}", align="center",
                             font=("Courier", 24))
            ball.goto(0, 0)
            ball.dx *= -1

        # Paddle and ball collisions
        if ball.xcor() < -340 and player_paddle.ycor() + 50 > ball.ycor() > player_paddle.ycor() - 50:
            ball.dx *= -1.01

        elif ball.xcor() > 340 and opponent_paddle.ycor() + 50 > ball.ycor() > opponent_paddle.ycor() - 50:
            ball.dx *= -1.01

        if ball.dx > 2:
            ball.dx = 2
        elif ball.dx < -2:
            ball.dx = -2

        if random.random() < 0.35:
            opponent_decession()

except SyntaxError:
    pass
