import turtle

# Create a turtle object
t = turtle.Turtle()

# Move the turtle forward by 100 units
t.forward(100)

# Retrieve the current heading of the turtle
current_heading = t.heading()

# Print the current heading
print("Current heading:", current_heading)

# Keep the window open until it's manually closed
turtle.done()