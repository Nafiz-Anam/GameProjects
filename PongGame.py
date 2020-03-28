import turtle

# making the field

field = turtle.Screen()
field.title("Game v0.1 by Nafiz")
field.bgcolor("black")
field.setup(width=800, height=600)
field.tracer(0)

# score

score_a = 0
score_b = 0

# stick a

stick_a = turtle.Turtle()
stick_a.speed(0)
stick_a.shape("square")
stick_a.color("blue")
stick_a.shapesize(stretch_wid=5, stretch_len=1)
stick_a.penup()
stick_a.goto(-350, 0)

# stick b

stick_b = turtle.Turtle()
stick_b.speed(0)
stick_b.shape("square")
stick_b.color("red")
stick_b.shapesize(stretch_wid=5, stretch_len=1)
stick_b.penup()
stick_b.goto(350, 0)

# main ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = .3
ball.dy = -.3

# score board

sBoard = turtle.Turtle()
sBoard.speed(0)
sBoard.color("white")
sBoard.penup()
sBoard.hideturtle()
sBoard.goto(0, 260)
sBoard.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# game function

def stick_a_up():
    y = stick_a.ycor()
    y += 20
    stick_a.sety(y)


def stick_a_down():
    y = stick_a.ycor()
    y -= 20
    stick_a.sety(y)


def stick_b_up():
    y = stick_b.ycor()
    y += 20
    stick_b.sety(y)


def stick_b_down():
    y = stick_b.ycor()
    y -= 20
    stick_b.sety(y)


# set key board

field.listen()
field.onkeypress(stick_a_up, "w")
field.onkeypress(stick_a_down, "s")
field.onkeypress(stick_b_up, "Up")
field.onkeypress(stick_b_down, "Down")

# main game loop

while True:
    field.update()

    # moving ball in random
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # boarding checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        sBoard.clear()  # clear the board every time
        sBoard.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                     font=("Courier", 24, "normal"))  # printing score on board

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        sBoard.clear()  # clear the board every time
        sBoard.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                     font=("Courier", 24, "normal"))  # printing score on board

    # stick and ball bounce

    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < stick_b.ycor() + 40 and ball.ycor() > stick_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < stick_a.ycor() + 40 and ball.ycor() > stick_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
