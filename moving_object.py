import turtle

wn = turtle.Screen()
wn.title("Moving Object with Turtle")
wn.bgcolor("black")
wn.setup(width=600, height=600)

square = turtle.Turtle()
square.shape("square")
square.color("white")
square.penup()
square.speed(0)

def move_up():
    y = square.ycor()
    square.sety(y + 20)

def move_down():
    y = square.ycor()
    square.sety(y - 20)

def move_left():
    x = square.xcor()
    square.setx(x - 20)

def move_right():
    x = square.xcor()
    square.setx(x + 20)

wn.listen()
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")

while True:
    wn.update()
