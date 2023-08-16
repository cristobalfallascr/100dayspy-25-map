import turtle
import pandas
screen = turtle.Screen()
screen.title('U.S. States Game')
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

states_coordinates = pandas.read_csv("50_states.csv")
#print(states_coordinates.state)

def write_state(name, x,y):
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.goto(x,y)
    state.write(name)



game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="Enter State's name:")

    match = states_coordinates[states_coordinates.state == answer_state]
    if len(match) > 0:
        name = match.iloc[0,0]
        x = match.iloc[0,1]
        y = match.iloc[0,2]
        print(name, x, y)
        write_state(name,x, y)






screen.exitonclick()