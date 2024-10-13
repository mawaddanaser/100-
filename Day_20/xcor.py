import turtle

# Create a turtle object
t = turtle.Turtle()

# Move the turtle to a specific position
t.goto(100, 50)

# Retrieve the x-coordinate of the turtle's current position
x_coordinate = t.xcor()
y_coordinate = t.ycor()
# Print the x-coordinate
print("X-coordinate:", x_coordinate)
print("y-coordinate:", y_coordinate)

# Keep the window open until it's manually closed
turtle.done()
