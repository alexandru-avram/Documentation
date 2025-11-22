import tkinter

# Create a window by creating a TK object
window = tkinter.Tk()
# Change the tile of the window
window.title("My first GUI program")
# Set the sixe
window.minsize(width=500, height=300)
# Add padding to your window
window.config(padx=20, pady=20)

# Creating components

# Label / Place the label on the window using pack()
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()
my_label.config(text = "New Text")
my_label.config(padx=50, pady=50)

# Entry / use .get() to return the text added in the entry
input = tkinter.Entry()
input.pack()
input.get()


# Button / use command to assign a function to the button
def button_clicked():
    new_text = input.get()
    my_label.config(text = new_text)

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()


# Using place, you can place the widget exactly where you want
my_label2 = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label2.place(x=100, y=200)


''' Gird is a concept where you image the program as a grid so that you can place the widgets in a specific grid
my_label3 = tkinter.Label(text="I am a label also", font=("Arial", 24, "bold"))
my_label3.grid(column=10, row=10)
'''


# Keep the window open until closed. Always to be put on the end of the script
window.mainloop()