from turtle import Turtle, Screen
import random


def pop_up(input_text):
  pop_up_text=Turtle()
  pop_up_text.pu()
  pop_up_text.hideturtle()
  pop_up_text.goto(x=-100, y=0)
  pop_up_text.write(font="center", arg= input_text)


screen = Screen()
screen.setup(width=500,height=400)
colors = ["blue","green","yellow","orange","red","purple"]
x=100
y= 100
dot_list=[]
for num in range(6):
  dot = Turtle()
  dot.hideturtle()
  dot.pu()
  dot.goto(x,y)
  dot.dot(20,colors[num])
  x -= 40
  dot_list.append(dot)
user_bet =""
while user_bet == "":
  user_bet = screen.textinput(title="Make your bet", prompt="Which turtle's color will win the race? Enter: ").lower()
else:
  for dot in dot_list:
    dot.clear()
is_race_on = False
x=-230
y=80
turtle_name =[]

for turtle_index in range(6):
  t = Turtle(shape="turtle")
  turtle_name.append(t)
  t.pu()
  t.color(colors[turtle_index])
  t.goto(x, y)
  y-=30


if user_bet:
  is_race_on = True

while is_race_on:
  for tur in turtle_name:
    if tur.xcor() > 230:
      is_race_on = False
      winning_turtle = tur.fillcolor()
      if user_bet == winning_turtle:
        text = f"You've won! The {winning_turtle} is the winner!"
        pop_up(text)
      else:
        text = f"You lose! The winner is {winning_turtle} turtle!"
        pop_up(text)


    random_distance= random.randint(0,10)
    tur.forward(random_distance)





screen.exitonclick()