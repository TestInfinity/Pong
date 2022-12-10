import random
import time
import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
player_score = 0
opponent_score = 0

# Player
player_paddle = turtle.Turtle()
player_paddle.speed(0)
player_paddle.shape("square")
player_paddle.color("white")
player_paddle.shapesize(stretch_wid=5, stretch_len=1)
player_paddle.penup()
player_paddle.goto(-350, 0)

# Opponent
opponent_paddle = turtle.Turtle()
opponent_paddle.speed(0)
opponent_paddle.shape("square")
opponent_paddle.color("white")
opponent_paddle.shapesize(stretch_wid=5, stretch_len=1)
opponent_paddle.penup()
opponent_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

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
        y += 20
        paddle.sety(y)


def paddle_down(paddle):
    y = paddle.ycor()
    if y > -290:
        y -= 20
        paddle.sety(y)


def opponent_decession():

    if ball.dx > 0:
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
                             font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        elif ball.xcor() < -350:
            opponent_score += 1
            scoreboard.clear()
            scoreboard.write(f"Player: {player_score}  Opponent: {opponent_score}", align="center",
                             font=("Courier", 24, "normal"))
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

        if random.random() < 0.25:
            opponent_decession()

except:
    pass