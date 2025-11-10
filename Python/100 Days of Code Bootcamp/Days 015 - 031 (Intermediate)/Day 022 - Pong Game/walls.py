from turtle import Turtle

class Wall(Turtle):
    def __init__(self, position=None, draw_net=False):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        # Stretch width controls height; stretch length controls width of the square
        self.shapesize(stretch_wid=1, stretch_len=60)  
        
        if position:
            self.goto(position)
        self.pendown()

        if draw_net:
            self.shapesize(stretch_wid=0.1, stretch_len=1)
            self.draw_net()
        
        
    def draw_net(self):
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=1)  
        self.goto(0, -400)
        self.setheading(90)  # Point the turtle upwards
        
        self.pensize(2)
        self.pencolor("white")
        self.forward(10)

        for _ in range(20):  # 20 dashes going up, adjust number for desired length
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

        
        

