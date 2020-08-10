# Star Crashers
import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(3)

score = 0
border = turtle.Turtle()
border.penup()
border.setpos(-350, -350)
border.pendown()
border.pensize(3)
border.color("white")

for side in range(4):
    border.forward(700)
    border.left(90)

border.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

max_stars = 10
stars = []

for count in range(max_stars):
    stars.append(turtle.Turtle())
    stars[count].color("red")
    stars[count].shape("circle")
    stars[count].penup()
    stars[count].speed(3)
    stars[count].setpos(random.randint(-350, 350), random.randint(-350, 350))

speed = 1

def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 1

def is_collison(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 20:
        return True
    else:
        return False
        stars[count].setpos(random.randint(-350, 350), random.randint(-350, 350))
        stars[count].right(random.randint(0, 360))



turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")


while True:
    player.forward(speed)

    if player.xcor() > 350 or player.xcor() < -350:
        player.right(180)

    if player.ycor() > 350 or player.ycor() < -350:
        player.right(180)


    for count in range(max_stars):
        stars[count].forward(3)

        if stars[count].xcor() > 340 or stars[count].xcor() < -340:
            stars[count].right(180)

        if stars[count].ycor() > 340 or stars[count].ycor() < -340:
            stars[count].right(180)

        if is_collison(player, stars[count]):
            stars[count].setpos(random.randint(-350, 350), random.randint(-350, 350))
            stars[count].right(random.randint(0, 360))
            score += 1
            border.undo()
            border.penup()
            border.hideturtle()
            border.setposition(-350, 355)
            score_string = "Score:%s"%score
            border.write(score_string, False, align="left", font=("Arial",14, "normal"))