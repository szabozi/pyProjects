"""
Drawing a snowflake with turtle
"""

import turtle

pat = turtle.Turtle()
pat.pensize(5)

for i in range(10):
    for y in range(2):
        pat.forward(100)
        pat.right(60)
        pat.forward(100)
        pat.right(120)
    pat.right(36)

input("Enter to exit")
