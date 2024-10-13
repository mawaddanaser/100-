from turtle import Turtle, Screen

import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
x_positions = [0, -20, -40]
segments = []
# Create snake
for turtle_index in range(0, 3):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(x=x_positions[turtle_index], y=0)
    segments.append(new_segment)

# Move snake
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)










screen.exitonclick()