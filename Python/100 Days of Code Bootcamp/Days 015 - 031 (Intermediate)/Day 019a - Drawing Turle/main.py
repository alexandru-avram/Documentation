import turtle

tim = turtle.Turtle()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.home()
    tim.clear()


# We have to use an even listener to wait for user inpuct
screen = turtle.Screen()

screen.listen() # this will listen
# we pass a function as an input without "()". This is called a higher order function
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = turn_left)
screen.onkey(key = "d", fun = turn_right)
screen.onkey(key = "c", fun = clear)


screen.exitonclick()