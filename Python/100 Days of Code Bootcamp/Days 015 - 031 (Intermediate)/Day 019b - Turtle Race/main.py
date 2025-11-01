import turtle
import random
from tkinter import messagebox

# Setup the screen
screen = turtle.Screen()
screen.setup(width=1000, height=500)
screen.title("Turtle Race")
user_guess = screen.textinput(title="Winning turle", prompt="Which turtle will win the race: ")


# Create turtles
tim_collors = ["purple", "blue", "green", "cyan", "orange", "red"]
turtles = []
initial_x = -450
finish_x = 450
y_position = 125

for turtle_index in range(0,6):
    tim = turtle.Turtle(shape="turtle")
    tim.color(tim_collors[turtle_index])
    tim.penup()
    tim.goto(initial_x, y_position)
    y_position -= 50
    turtles.append(tim)

if user_guess:
    race_on = True

while race_on:

    for turtle in turtles:
        if turtle.xcor() >= finish_x:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                messagebox.showinfo("CONGRATS", f"You won! The {winning_color} turle is the winner!")
            else:
                messagebox.showinfo("SORRY", f"You lost! The {winning_color} turle is the winner!")

        turtle.forward(random.randint(0,10))


screen.exitonclick()