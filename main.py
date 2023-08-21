import turtle
import pandas
screen = turtle.Screen()
screen.title('U.S. States Game')
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

states_coordinates = pandas.read_csv("50_states.csv")
all_states = states_coordinates.state.to_list()
print(all_states)

def write_state(name, x,y):
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.goto(x,y)
    state.write(name)



game_is_on = True
guessed_states = []

while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="Enter State's name:")
    if answer_state != 'exit':

        match = states_coordinates[states_coordinates.state == answer_state]
        if answer_state in all_states:
            guessed_states.append(answer_state)
            name = match.iloc[0,0]
            x = match.iloc[0,1]
            y = match.iloc[0,2]
            print(name, x, y)
            write_state(name,x, y)
    else:
        states_to_learn = [state for state in all_states if state not in guessed_states]
        game_is_on = False

print("States you know: " + str(len(guessed_states)))
print(guessed_states)

print("States you dont know: " + str(len(states_to_learn)))
print(states_to_learn)



screen.exitonclick()