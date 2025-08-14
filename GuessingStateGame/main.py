import turtle
from turtle import Turtle, Screen
import pandas




screen = Screen()
screen.title("U.S state Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
correct_answer = []
counter = 0

t = Turtle()
t.hideturtle()
t.penup()

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{counter}/50 States Correct", prompt="Whats another state's name?").title()

    if answer_state == "Exit":
        break

    if (answer_state in state_list) and (answer_state not in correct_answer):
        correct_answer.append(answer_state)
        counter += 1
        row_of_state = data[data["state"] == answer_state]
        x_location = int(row_of_state["x"])
        y_location = int(row_of_state["y"])
        t.goto(x_location,y_location)
        t.write(arg=answer_state, align="center", font=("Arial", 12, "normal"))

    if counter == 50:
        game_is_on = False

missed_states = []
for names in state_list:
    if names not in correct_answer:
        missed_states.append(names)

print(missed_states)

new_data = pandas.DataFrame(missed_states)
new_data.to_csv("states_to_learn.csv")
