# import turtle
#
# # Create a turtle object
# t = turtle.Turtle()
#
# # Set the tracer to 0 to speed up drawing
# turtle.tracer()
#
# # Draw a square
# for _ in range(4):
#     t.forward(100)
#     t.right(90)
#
# # Update the screen to display the drawing
# turtle.update()
#
# # Keep the window open until it's manually closed
# turtle.done()

###########################

import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a circle with different tracer values
for tracer_value in [0, 1, 5, 10]:
    # Set the tracer value
    turtle.tracer(tracer_value)

    # Draw the circle
    for _ in range(36):
        t.forward(10)
        t.left(10)

    # Update the screen to display the drawing
    turtle.update()

    # Reset the turtle position
    t.penup()
    t.goto(0, 0)
    t.pendown()

# Keep the window open until it's manually closed
turtle.done()