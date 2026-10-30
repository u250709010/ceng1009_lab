# def sumTo(n):
#     return n * (n + 1) / 2
# print(sumTo(10))
# n = int(input("Please Enter a Number:"))
# print("Smu is", sumTo(n))


# import turtle
#
# wn=turtle.Screen()
# wn.bgcolor("lightgreen")
#
# a=turtle.Turtle()
# a.color("hotpink")
# a.pensize(2)
#
# def drawStar(a, n, size):
#     angle= 180-180/n
#     for i in range(n):
#         a.forward(size)
#         a.left(angle)
#
# drawStar(a, 10, 30)
#
# wn.exitonclick()



# def sumTo(n):
#     total = 0
#     for i in range(1, n+1):
#         total = total + i
#     return total
# n = int(input("Please Enter a Number:"))
# print("Sum is", sumTo(n))



# def mySqrt(n):
#     guess = n / 2
#     for i in range(20):
#         guess = (0.5) * (guess + n / guess)
#     return guess
# n = int(input("Please enter a positive integer:"))
# print("the Result is:", mySqrt(n))
# print("the Result is:", mySqrt(mySqrt(n)))

# import turtle
#
# wn = turtle.Screen()
#
# t = turtle.Turtle()
# t.color("purple")
# t.pensize(2)
# t.speed(1)
#
# def drawSprite(someturtle, legs, lenght):
#     angle = 360/legs
#     for i in range(legs):
#         someturtle.forward(lenght)
#         someturtle.backward(lenght)
#         someturtle.left(angle)
#
# def fancySquare(t, size):
#     for corner in range(4):
#         drawSprite(t, 8, 20)
#         t.fd(size)
#         t.left(90)
#
# fancySquare(t, 150)
#
# wn.exitonclick()

# import turtle
#
# def drawTip(t, size):
#     t.begin_fill()
#     t.lt(90)
#     t.fd(size/2)
#     t.rt(120)
#     t.fd(size)
#     t.rt(120)
#     t.fd(size)
#     t.rt(120)
#     t.fd(size/2)
#     t.rt(90)
#     t.end_fill()
#
# def drawSpriteWithTips(someturtle, legs, length):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.fd(length)
#         drawTip(someturtle, 10)
#         someturtle.bk(length)
#         someturtle.lt(angle)
# def fancySquare(t, size):
#     for corner in range(4):
#         drawSpriteWithTips(t, 8, 20)
#         t.fd(size)
#         t.lt(90)
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
# t.speed(100)
# t.pensize(3)
# fancySquare(t, 100)
# wn.exitonclick()



# def checkSign(x):
#     if x >= 0:
#         return "the Number is Positive"
#     elif x < 0:
#         return "the Number is Negative"
#     else:
#         return "the Number is Zero"
# numbers = [-7, 5, 0]
# for number in numbers:
#     print(number, checkSign(number))
# n = int(input("Enter a Number:"))
# print(checkSign(n))



import turtle

def drawBar(t, height, gap):
    t.penup()
    t.lt(90)
    t.fd(height + gap)
    t.write(" " + str(height))
    t.bk(height + gap)
    t.rt(90)
    t.pendown()

    t.begin_fill()
    t.lt(90)
    t.fd(height)
    t.rt(90)
    t.fd(40)
    t.rt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()


def barChart(data):
    maxheight = max(data)
    num_bars = len(data)
    border = 10
    gap = (maxheight - border) / 25

    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    right = 40 * num_bars + border
    top = maxheight + 4 * border
    wn.setworldcoordinates(-border, -border, right, top)

    t = turtle.Turtle()
    t.color("blue")
    t.fillcolor("red")
    t.pensize(3)

    for height in data:
        drawBar(t, height, gap)

    wn.exitonclick()

data = [48, 117, 200, 240, 160, 260, 220]
barChart(data)