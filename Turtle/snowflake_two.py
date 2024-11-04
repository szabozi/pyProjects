"""
Drawing another snowflake with turtle
"""

import turtle

pat = turtle.Turtle()
turtle.Screen().bgcolor("#ADD8E6")

pat.pensize(5)
pat.penup()
pat.forward(90)
pat.left(45)
pat.pendown()


def branch():
    for i in range(3):
        for y in range(3):
            pat.forward(30)
            pat.backward(30)
            pat.right(45)
        pat.left(90)
        pat.backward(30)
        pat.left(45)
    pat.right(90)
    pat.forward(90)


for x in range(8):
    branch()
    pat.left(45)


input("Enter to exit..")













