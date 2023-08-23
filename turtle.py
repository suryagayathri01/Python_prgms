from turtle import *
t = Turtle()


def drawSquare(t, x, y, length):
    """Draws a square with the given turtle t, an upper-left corner point (x, y), and a side's length."""


t.up()
t.goto(x, y)
t.setheading(270)
t.down()
for count in range(4):
t.forward(length)
t.left(90)

drawSquare(t, 0, 0, 50)
