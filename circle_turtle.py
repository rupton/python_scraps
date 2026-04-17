import turtle
import math
''' t = turtle.Turtle()
t.circle(100)  # radius in pixels

turtle.done()
'''


t = turtle.Turtle()
t.speed(0)

radius = 100

# Lift pen so it doesn't draw from (0,0) to the circle
t.penup()

# Start at angle 0
x = radius * math.cos(math.radians(0))
y = radius * math.sin(math.radians(0))
t.goto(x, y)

# Put pen down and trace the circle
t.pendown()

for angle in range(1, 361):
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    t.goto(x, y)

turtle.done()