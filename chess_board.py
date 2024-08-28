import turtle

screen = turtle.Screen()
screen.title("Chess Board")
screen.setup(width=600, height=600)

board_turtle = turtle.Turtle()
board_turtle.speed(0)
board_turtle.penup()

square_size = 50

# Define colors
colors = ["black", "white"]

# Draw the chessboard
for row in range(8):
    for col in range(8):
        # Set position for each square
        x = col * square_size - 200
        y = row * square_size - 200
        board_turtle.goto(x, y)
        
        color = colors[(row + col) % 2]
        
        board_turtle.fillcolor(color)
        board_turtle.begin_fill()
        for _ in range(4):
            board_turtle.pendown()
            board_turtle.forward(square_size)
            board_turtle.left(90)
        board_turtle.end_fill()
        board_turtle.penup()

board_turtle.hideturtle()

turtle.done()
