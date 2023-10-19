import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

# import colorgram
# color = colorgram.extract('image.jpeg',20)
#
# rgb_color = []
#
# for each in color:
#     r = each.rgb.r
#     b = each.rgb.b
#     g = each.rgb.g
#     rgb_color.append((r, b, g))
my_screen = Screen()
color_list =[(213, 96, 154), (52, 132, 107), (179, 31, 77), (202, 31, 142), (115, 171, 155), (124, 99, 79),
             (122, 156, 175), (229, 239, 236), (226, 131, 198), (242, 244, 247), (192, 108, 87), (11, 64, 50),
             (55, 19, 38), (45, 126, 168), (47, 123, 127), (200, 143, 121), (168, 29, 21), (228, 77, 92)]


tim = Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.pu()


def draw_hirst_painting():
    x= -225
    y= -225
    tim.goto(x, y)
    for i in range(10):
        i=1
        while i < 10:
            tim.dot(20,random.choice(color_list))
            tim.forward(50)
            tim.dot(20)
            i += 1
        y += 50
        tim.goto(x, y)

draw_hirst_painting()
