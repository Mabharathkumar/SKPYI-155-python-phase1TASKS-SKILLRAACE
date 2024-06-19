import turtle

# Setting up the screen
screen = turtle.Screen()
screen.title("Indian Flag")
screen.setup(width=800, height=600)

# Create a turtle object
flag = turtle.Turtle()
flag.speed(3)  # Set the speed of the turtle

# Function to draw a rectangle
def draw_rectangle(color, width, height):
    flag.color(color)
    flag.begin_fill()
    for _ in range(2):
        flag.forward(width)
        flag.right(90)
        flag.forward(height)
        flag.right(90)
    flag.end_fill()

# Move the turtle to the starting position
flag.penup()
flag.goto(-150, 100)
flag.pendown()

# Dimensions for the flag
flag_width = 300
flag_height = 200

# Draw the saffron rectangle
draw_rectangle("orange", flag_width, flag_height / 3)

# Move to the position for the white stripe
flag.penup()
flag.goto(-150, 100 - (flag_height / 3))
flag.pendown()

# Draw the white rectangle
draw_rectangle("white", flag_width, flag_height / 3)

# Move to the position for the green stripe
flag.penup()
flag.goto(-150, 100 - (2 * flag_height / 3))
flag.pendown()

# Draw the green rectangle
draw_rectangle("green", flag_width, flag_height / 3)

# Function to draw the Ashoka Chakra
def draw_ashoka_chakra(radius):
    flag.penup()
    # Calculate the center position of the white stripe
    center_y = 100 - (flag_height / 3) - (flag_height / 6)
    flag.goto(0, center_y - radius)
    flag.pendown()
    flag.color("navy")
    flag.circle(radius)
    
    # Drawing 24 spokes
    flag.penup()
    flag.goto(0, center_y)
    flag.setheading(0)
    for _ in range(24):
        flag.pendown()
        flag.forward(radius)
        flag.penup()
        flag.goto(0, center_y)
        flag.right(15)

# Draw the Ashoka Chakra
draw_ashoka_chakra(30)

# Hide the turtle
flag.hideturtle()

# Keep the window open
turtle.done()
