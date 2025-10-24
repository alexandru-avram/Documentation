import colorgram
from pathlib import Path
import turtle
import random

"""
The goal of this program is to create a spot paintaing:
- extract an image
- extract the colors from the image using colorgram
- paste the colors in a list
- use the list of colors with turle to create the painting
"""

# Folder where *this* .py file lives
HERE = Path(__file__).resolve().parent
my_image = HERE / "image.jpg"

# colorgram wants a path (string) or file-like
colors = colorgram.extract(my_image, 25)  # cast to str just to be safe

# Create a new list to hold the colors
rgb_colors = []

# Create a for loop to extract the colors and append them into a list in the form of a tuple
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))


# First, create a turtle object. Hide it, hide the pen.
turtle.colormode(255)
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()

# Set the position of the turle
pos_x = -225
pos_y = -225
tim.setx(pos_x)
tim.sety(pos_y)



# Design the for loop to create the painting
for _ in range(0, 10):
    for _ in range(0, 10):
        tim.dot(25, random.choice(rgb_colors))
        tim.forward(50)

    tim.setx(pos_x)
    pos_y += 50
    tim.sety(pos_y)


screen = turtle.Screen()
screen.exitonclick()