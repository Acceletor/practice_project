import turtle
import pandas
from showlocation import Showlocation

screen = turtle.Screen()

screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



showlocation = Showlocation()

data = pandas.read_csv("50_states.csv")
all_city = data.state.to_list()

list_correct_state = []


while len(list_correct_state) < 50:

    answer_state = screen.textinput(title=f"{len(list_correct_state)}/50 States Correct",prompt="What's another state's name?").title()
    if answer_state == "Exit":
        screen.tracer(0)
        didnotguess = [n for n in all_city if n not in list_correct_state]
        for city in didnotguess:
            state_data = data[data.state == city]
            x = int(state_data.x)
            y = int(state_data.y)
            location=(x, y)
            showlocation.color("red")
            showlocation.speed("fastest")
            showlocation.print_text(city, location)
        screen.update()
        break


    if answer_state in all_city:
        list_correct_state.append(answer_state)
        state_data = data[data.state == answer_state]
        x = data.loc[data.state == answer_state].x.item()
        y = data.loc[data.state == answer_state, "y"].item()
        # x = int(state_data.x)
        # y = int(state_data.y)
        location = (x,y)
        showlocation.print_text(answer_state,location)



new_data = pandas.DataFrame(didnotguess)
new_data.to_csv("state_to_learn.txt")
print(new_data)

screen.mainloop()

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)