from turtle import Turtle, Screen
from walls import Wall
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import _tkinter
import time


# Setup the screen
screen = Screen()
screen.setup(width=1210, height=820)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


upper_wall = Wall((0, 400))  # Top wall at y=400 with centered x=0
lower_wall = Wall((0, -400)) # Bottom wall at y=-400
wall_net = Wall(draw_net=True)


# Setup the paddles
paddle1 = Paddle((-580, 0))
paddle2 = Paddle((580, 0))
screen.listen()
screen.onkey(paddle1.go_up, "w")
screen.onkey(paddle1.go_down, "s")
screen.onkey(paddle2.go_up, "Up")
screen.onkey(paddle2.go_down, "Down")


# Setup the ball
ball = Ball()

# Setup the scoreboard
scoreboard = ScoreBoard()

game_on = True
while game_on:
    try:
        time.sleep(0.025)  # faster update rate for smoother movement
        ball.move()        
        screen.update()

        # Detect collision with the walls
        if ball.ycor() >= upper_wall.ycor() - 10 or ball.ycor() <= lower_wall.ycor() + 10:
            ball.bounce_y()

        # Detect collision with paddle2
        if ball.distance(paddle2) < 20 and ball.xcor() > 480:
            ball.bounce_x()
        # Detect collision with paddle1
        elif ball.distance(paddle1) < 20 and ball.xcor() < -480:
            ball.bounce_x()

        # Detect a score
        if ball.xcor() > 600:
            ball.reset_position()
            scoreboard.p1_point()
        elif ball.xcor() < -600:
            ball.reset_position()
            scoreboard.p2_point()

    except _tkinter.TclError:
        # This error occurs when the turtle window is closed.
        print("Turtle window closed. Exiting game.")
        game_on = False