import turtle

screen = turtle.Screen()
screen.title("Turtle Race - Two Player Game")
screen.bgcolor("lightblue")

player1 = turtle.Turtle()
player1.color("red")
player1.shape("turtle")
player1.penup()
player1.goto(-200, 100)
player1.pendown()

player2 = turtle.Turtle()
player2.color("blue")
player2.shape("turtle")
player2.penup()
player2.goto(-200, -100)
player2.pendown()

finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(200, 150)
finish_line.pendown()
finish_line.right(90)
finish_line.forward(300)
finish_line.hideturtle()

def move_player1():
    player1.forward(20)

def move_player2():
    player2.forward(20)

def check_winner():
    if player1.xcor() >= 200:
        turtle.clearscreen()
        screen.bgcolor("lightgreen")
        turtle.write("Player 1 Wins!", align="center", font=("Arial", 24, "bold"))
    elif player2.xcor() >= 200:
        turtle.clearscreen()
        screen.bgcolor("lightgreen")
        turtle.write("Player 2 Wins!", align="center", font=("Arial", 24, "bold"))

screen.listen()
screen.onkey(move_player1, "w")  
screen.onkey(move_player2, "Up")  

while True:
    check_winner()
    screen.update()
