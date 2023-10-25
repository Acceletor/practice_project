from turtle import Turtle

class Showlocation(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()


    def print_text(self,city,location):
        self.goto(location)
        self.write(arg=city,align="center", font=("arial",11,"normal"))