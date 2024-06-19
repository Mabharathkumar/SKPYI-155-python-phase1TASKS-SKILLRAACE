import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Example")
screen.bgcolor("white")

# Create a turtle named "t"
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

# Move the turtle forward by 100 units
t.forward(100)

# Turn the turtle 90 degrees to the right
t.right(90)

# Move the turtle forward by 50 units
t.forward(50)

# Close the window when clicked
screen.exitonclick()
