# for i in range(100):
#     print("We like Python's turtles")

# for i in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
#     print(f"One of the months of the year is {i} ")

# for i in [ 12, 10, 32, 3, 66, 17, 42, 99, 20]:
#     print(i)
#     print(i**2)

# import turtle
#
# t = turtle.Turtle()
# screen = turtle.Screen()
#
# t.penup()
# t.goto(-300, 0)
# t.pendown()
#
# for i in range(3):
#      t.forward(100)
#      t.left(120)
#
# t.penup()
# t.goto(-100, 0)
# t.pendown()
#
# for i in range(4):
#     t.forward(100)
#     t.left(90)
#
# t.penup()
# t.goto(100 , 0)
# t.pendown()
#
# for i in range(6):
#     t.forward(100)
#     t.left(60)
#
# t.penup()
# t.goto(-100, 150)
# t.pendown()
#
# for i in range(8):
#     t.forward(100)
#     t.left(45)
#
# screen.exitonclick()

# import turtle
#
# t = turtle.Turtle()
# screen = turtle.Screen()
#
# screen.bgcolor("lightgreen")
# t.shape("turtle")
# t.color("blue")
# t.shapesize(1)
# t.stamp()
#
# t.penup()
#
# for i in range(12):
#     t.forward(125)
#     t.pendown()
#     t.forward(15)
#
#     t.penup()
#     t.forward(25)
#     t.stamp()
#     t.backward(165)
#     t.left(30)
#
# screen.exitonclick()

# import turtle
#
# Pirate=turtle.Turtle()
# screen=turtle.Screen()
#
# turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]
#
# for angle in turns:
#     Pirate.left(angle)
#     Pirate.forward(100)
#
# print("Pirate final heading", Pirate.heading())
#
# screen.exitonclick()