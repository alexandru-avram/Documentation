import turtle as tur
import random

timmy = tur.Turtle()
tur.colormode(255)

timmy.shape("turtle")
timmy.color("blue")
timmy.speed("fastest")
timmy.pensize(3)

def random_color():
    red = random.randint(1, 255)
    blue = random.randint(1, 255)
    green = random.randint(1, 255)

    color = (red, blue, green)
    return color



""" Turle draws a square

for _ in range (0,4):
    for _ in range (0, 5):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

    timmy.left(90)
"""

""" Turle draws a triangle, square, pentagon, sextagon, septagon, octogon, decagon
red = 0
green = 0
blue = 0

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360/ num_sides
        timmy.forward(100)
        timmy.right(angle)


for shape_side_n in range(3, 10):

    if red + 0.1 < 1:
        red += 0.1
    else:
        red = 0.1

    if green + 0.2 < 1:
        green += 0.2
    else:
        green = 0.1

    if blue + 0.3 < 1:
        blue += 0.3
    else:
        blue = 0.1

    timmy.pencolor(red, green, blue)
    draw_shape(shape_side_n)
"""

""" Turle walks randomly

angle_choice = [0, 90, 180, 270, 360]

for _ in range(100):

    timmy.pencolor(random_color())
    steps = 50
    angle = random.choice(angle_choice)

    pen_size = random.randint(3,6)
    timmy.pensize(pen_size)

    timmy.right(angle)
    timmy.forward(steps)
"""

""" Turle draws a spirograph """

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.pencolor(random_color())
        timmy.setheading(timmy.heading()+10)
        timmy.circle(100)

draw_spirograph(10)

screen = tur.Screen()
screen.exitonclick()