# import turtle
# timmy = turtle.Turtle()

# from turtle import Turtle, Screen
# temmy = Turtle()
# print(temmy)
# temmy.shape("turtle")
# temmy.color("DeepPink")
# temmy.(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pochemon Name", ["Scatterbug", "Pichu", "Simipour"])
table.add_column("Type", ["bug", "electric", "Water"])
print(table.align)
table.align = "l"
print(table)

