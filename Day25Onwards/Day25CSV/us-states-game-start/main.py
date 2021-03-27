from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S.States Game")
image = "blank_states_img.gif"
screen.addshape(image)
back = Turtle()
back.shape(image)
timmy = Turtle()
timmy.penup()
timmy.hideturtle()
data = pandas.read_csv("./50_states.csv")
guessed_states = []
all_states = data.state.to_list()
missing_states=[]

while len(guessed_states) < 50:
    stateName = screen.textinput(f"{len(guessed_states)}/50 States Done", "Enter Name of state")
    stateFound = data[data.state == stateName.title()]
    if stateName.title() == "Exit":
        break
    elif len(stateFound) == 0:
        print("Wrong name")
    else:
        new_x = stateFound.x.item()
        new_y = stateFound.y.item()
        print(new_x, new_y)
        timmy.goto(new_x, new_y)
        timmy.write(stateName)
        guessed_states.append(stateName.title())


missing_states = [state for state in all_states if state not in guessed_states]
print(missing_states)
new_missed_csv = pandas.DataFrame(missing_states)
print(all_states)
print(guessed_states)
new_missed_csv.to_csv("MissedStateNames.csv")

screen.exitonclick()
# def get_mouse_click_coor(x, y ):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
