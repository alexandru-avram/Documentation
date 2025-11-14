import turtle
import pandas as pd

# OPEN IMAGE and convert the image into a turtle shape
from pathlib import Path
HERE = Path(__file__).resolve().parent
my_image = HERE / "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US States")
screen.addshape(str(my_image))
turtle.shape(str(my_image))


""" 
# Get coordonates for a mouse click
def get_mouse_click_coor (x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
"""

data = pd.read_csv(HERE/"50_states.csv")


# Transform the dataFrame column into a list
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50", 
                                    prompt = "Write the name of a US State:")
    
    if answer_state is None:  # User clicked Cancel
        missing_states = []
        for state in [state.lower() for state in all_states]:
            if state not in [state.lower() for state in guessed_states]:
                missing_states.append(state.title())
        
        # Save states not guessed to a new .csv
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv(HERE/"states.to_learn.csv")
        break


    elif answer_state.lower() in [state.lower() for state in all_states]:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        # Save the state data line in a variable (including name, xcor, ycor)
        state_data = data[data.state.str.lower() == answer_state.lower()]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

screen.exitonclick()
