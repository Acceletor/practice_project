from turtle import Turtle
START_POSITION =[(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_body(position)

    def add_body(self,position):
        new_body=Turtle("square")
        new_body.pu()
        new_body.color("white")
        new_body.goto(position)
        self.body.append(new_body)

    def extend(self):
        # add segment to snake
        self.add_body(self.body[-1].position())
    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def reset(self):
        for seg in self.body:
            seg.goto(1000,1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]