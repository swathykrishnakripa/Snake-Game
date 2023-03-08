import turtle
import time
import random

delay = 0.1
segments = []
score = 0
high_score = 0

# screen

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# snake head

head = turtle.Turtle()
head.shape("square")
head.color("green")
head.speed(0)
head.penup()
head.shapesize(1, 1)
head.goto(0, 0)
head.direction = "stop"

# food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(1, 1)
food.goto(0, 100)

# score

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Score : 0  High Score : 0", align="center", font=("Courier", 18, "normal"))


# key directions

def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

while True:
    wn.update()
# check collision at border
    if head.xcor() > 290 or head.xcor() < - 290 or head.ycor() > 290 or head.ycor() < - 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
    
        for seg in segments:
            seg.goto(1000, 1000)

        # clear the segment list
        segments.clear()

        score = 0
        delay = 0.1

        # reset the score
        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score, high_score), align="center",
                  font=("Courier", 20, "normal"))

    # check collision with food
    if head.distance(food) < 15:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # adding segments
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        # shorten delay
        delay -= 0.001
        # increase score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score, high_score), align="center",
                      font=("Courier", 20, "normal"))

    # move the end segment first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # move segments 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

# check for collision with body part
    for seg in segments:
        if seg.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"

            # hide the segment
            for seg in segments:
                seg.goto(1000, 1000)

            # clear the segment list
            segments.clear()
            score = 0
            delay = 0.1

            # reset the score display
            pen.clear()
            pen.write("Score : {}  High Score : {}".format(score, high_score), align="center",
                      font=("Courier", 20, "normal"))
    time.sleep(delay)

wn.mainloop()
