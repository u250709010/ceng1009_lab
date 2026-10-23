import turtle

# -- Setup --
bro = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("lightgreen")

# -- Function --
def drawPoly(someturtle, somesides, somesize):
    angle = 360 / somesides
    for i in range(somesides):
        someturtle.fd(somesize)
        someturtle.lt(angle)

def drawSpiral(someturtle, angle):
    size = 1
    for i in range(100):
        someturtle.fd(size)
        someturtle.right(angle)
        size = size + 2

def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)

def drawStar (someturtle, size):
    for i in range(5):
        someturtle.fd(size)
        someturtle.right(144)

def drawSprite (someturtle, legs, lenght):
    angle = 360 / legs
    for i in range(legs):
        someturtle.fd(lenght)
        someturtle.back(lenght)
        someturtle.left(angle)

# # --  Exercise1 --
# bro.pencolor("hotpink")
# bro.pensize(3)
# drawPoly(bro, 8, 50)



# -- Exercise2 --
# bro.pencolor("darkblue")
# bro.pensize(3)
# for i in range(20):
#     drawPoly(bro, 4, 100)
#     bro.left(18)



# # -- Exercise3 --
# bro.pencolor("darkblue")
# bro.pensize(2)
# bro.penup()
# bro.goto(-200, 0)
# bro.pendown()
# drawSpiral(bro, 90)
#
# bro.penup()
# bro.goto(150, 0)
# bro.pendown()
# drawSpiral(bro, 89)



# # -- Exercise4 --
# drawEquitriangle(bro, 100)



# # -- Exercise5 --
# bro.color("hotpink")
# for i in range(5):
#     drawStar(bro, 50)
#     bro.penup()
#     bro.fd(250)
#     bro.right(144)
#     bro.pendown()



# # -- Exercise5 --
# drawSprite(bro, 15, 120)


# -- Finish --
screen.exitonclick()