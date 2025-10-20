import turtle

# Create a Screen object
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Click to Exit")

# Create a Turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("blue")
pen.speed(1)

# Draw something
pen.forward(100)
pen.left(90)
pen.forward(100)

# Keep the window open until a click and then close it
screen.exitonclick()